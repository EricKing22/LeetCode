import math
from dataclasses import dataclass
from typing import Optional, Tuple

import torch
import torch.nn as nn


@dataclass
class SimpleRoPEConfig:
    hidden_size: int = 64
    num_attention_heads: int = 8
    max_position_embeddings: int = 4096
    rope_theta: float = 10000.0  # RoPE base/theta
    head_dim: Optional[int] = None  # 默认 hidden_size // num_attention_heads
    attention_scaling: float = 1.0  # vanilla RoPE 是 1.0


class RotaryEmbedding(nn.Module):
    """
    - 输入: x (用来提供 dtype/device), position_ids
    - 输出: cos, sin (shape = [B, S, head_dim])
    """

    def __init__(self, config: SimpleRoPEConfig, device: Optional[torch.device] = None):
        super().__init__()
        self.config = config

        self.head_dim = config.head_dim or (config.hidden_size // config.num_attention_heads)
        assert self.head_dim % 2 == 0, "head_dim 必须是偶数 (RoPE 以 2 为步长构造频率)"

        self.max_seq_len_cached = config.max_position_embeddings
        self.original_max_seq_len = config.max_position_embeddings

        inv_freq = self._compute_inv_freq(
            dim=self.head_dim,
            base=config.rope_theta,
            device=device,
        )
        print("inv_freq", inv_freq)
        # register_buffer 跟随 .to(device) / .cuda(), 并且不会被当作参数训练
        self.register_buffer("inv_freq", inv_freq, persistent=False)

        self.attention_scaling = float(config.attention_scaling)

    @staticmethod
    def _compute_inv_freq(dim: int, base: float, device: Optional[torch.device]) -> torch.Tensor:
        # shape: [dim/2]
        half_idx = torch.arange(0, dim, 2, dtype=torch.float32, device=device)  # 0, 2, 4...
        inv_freq = 1.0 / (base ** (half_idx / dim))
        return inv_freq  # [dim/2]

    @torch.no_grad()
    def forward(
            self,
            x: torch.Tensor,
            B: int,  # batch_size
            position_ids: torch.Tensor = None,
            debug: bool = False,
            return_intermediates: bool = False,
    ):
        """
        x: q/k, 只用来提供 device/dtype
           常见 shape: [B, S, ...], 这里不强制
        position_ids: [B, S] (int/long)
        """
        if position_ids is None:
            position_ids = torch.arange(self.original_max_seq_len).unsqueeze(0).repeat(B, 1)  # [B, S]

        # inv_freq: [D/2] -> [1, D/2, 1] -> expand 到 batch
        inv_freq_expanded = self.inv_freq[None, :, None].to(device=x.device, dtype=torch.float32)
        inv_freq_expanded = inv_freq_expanded.expand(position_ids.shape[0], -1, 1)  # [B, D/2, 1]

        # position_ids: [B, S] -> [B, 1, S]
        pos = position_ids[:, None, :].to(device=x.device, dtype=torch.float32)  # [B, 1, S]

        # freqs: [B, D/2, 1] @ [B, 1, S] -> [B, D/2, S] -> transpose -> [B, S, D/2]
        freqs = torch.matmul(inv_freq_expanded, pos).transpose(1, 2)  # [B, S, D/2]

        if debug:
            print("freqs_1", freqs)

        # emb: 把 freqs 复制拼接起来得到 [B, S, D]
        emb = torch.cat((freqs, freqs), dim=-1)  # [B, S, D]

        if debug:
            print("freqs_2", emb[0, :4, :])

        cos = emb.cos() * self.attention_scaling
        sin = emb.sin() * self.attention_scaling

        # 按 x 的 dtype 返回
        cos = cos.to(dtype=x.dtype)
        sin = sin.to(dtype=x.dtype)

        if debug:
            def stat(name, t):
                print(
                    f"{name:>18}  shape={tuple(t.shape)}  dtype={t.dtype}  device={t.device}  "
                    f"min={t.min().item():+.4f}  max={t.max().item():+.4f}"
                )

            stat("inv_freq", self.inv_freq)
            stat("inv_freq_expanded", inv_freq_expanded)
            stat("position_ids", position_ids)
            stat("pos(float)", pos)
            stat("freqs", freqs)
            stat("emb", emb)
            stat("cos", cos)
            stat("sin", sin)

        if return_intermediates:
            return cos, sin, {
                "inv_freq_expanded": inv_freq_expanded,
                "pos": pos,
                "freqs": freqs,
                "emb": emb,
            }

        return cos, sin


def rotate_half(x):
    x1 = x[..., : x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2:]
    return torch.cat((-x2, x1), dim=-1)


def apply_rotary_pos_emb(q, k, cos, sin, position_ids=None, unsqueeze_dim=1):
    cos = cos.unsqueeze(unsqueeze_dim)
    sin = sin.unsqueeze(unsqueeze_dim)
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed


if __name__ == "__main__":
    torch.set_printoptions(precision=4, sci_mode=False)
    cfg = SimpleRoPEConfig(
        hidden_size=64,
        num_attention_heads=8,
        max_position_embeddings=4096,
        rope_theta=10000.0,
        attention_scaling=1.0,
    )
    rope = RotaryEmbedding(cfg)

    B = 1
    S = 4096
    H = cfg.num_attention_heads
    D = cfg.head_dim or (cfg.hidden_size // cfg.num_attention_heads)

    # 构造 q/k: [B, heads, seq_len, head_dim]
    torch.manual_seed(0)
    q = torch.randn(B, H, S, D, dtype=torch.float16)
    k = torch.randn(B, H, S, D, dtype=torch.float16)

    # 生成 cos/sin; 传入 q 只是为了确定 device
    cos, sin, inter = rope(q, B, debug=True, return_intermediates=True)

    # 应用 RoPE
    q_rope, k_rope = apply_rotary_pos_emb(q, k, cos, sin, unsqueeze_dim=1)

    print("\n===== shapes =====")
    print("q       ", q.shape)
    print("k       ", k.shape)
    print("cos     ", cos.shape)
    print("sin     ", sin.shape)
    print("q_rope  ", q_rope.shape)
    print("k_rope  ", k_rope.shape)