import torch
import torch.nn as nn


def rotate_half(x):
    # 1. 把最后一维切成前半和后半。
    x1 = x[..., : x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2 :]

    # 2. (x1, x2) -> (-x2, x1)。
    return torch.cat((-x2, x1), dim=-1)


class RotaryEmbedding(nn.Module):
    def __init__(self, head_dim, base=10000.0):
        super().__init__()
        # 1. RoPE 每两个维度共用一个频率。
        assert head_dim % 2 == 0
        self.head_dim = head_dim

        # 2. inv_freq: [D/2]，和 Q39 的写法保持一致。
        self.inv_freq = 1.0 / (base ** (torch.arange(0, head_dim, 2).float() / head_dim))

    def forward(self, q, k, position_ids):
        # 3. q/k: [B, H, S, D]，position_ids: [B, S]。

        # 4. freqs: [B, S, 1] * [D/2] -> [B, S, D/2]。
        freqs = position_ids.float().unsqueeze(-1) * self.inv_freq

        # 5. emb: [B, S, D/2] -> [B, S, D]。
        emb = torch.cat((freqs, freqs), dim=-1)

        # 6. cos/sin: [B, S, D] -> [B, 1, S, D]，广播到所有 head。
        cos = emb.cos().unsqueeze(1)
        sin = emb.sin().unsqueeze(1)

        # 7. RoPE 旋转公式：x * cos + rotate_half(x) * sin。
        q_embed = q * cos + rotate_half(q) * sin
        k_embed = k * cos + rotate_half(k) * sin
        return q_embed, k_embed


if __name__ == "__main__":
    q = torch.randn(2, 4, 8, 16)
    k = torch.randn(2, 4, 8, 16)
    position_ids = torch.arange(8).unsqueeze(0).expand(2, -1)
    print(RotaryEmbedding(16)(q, k, position_ids)[0].shape)
