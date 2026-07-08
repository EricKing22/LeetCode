import math

import torch
import torch.nn as nn


class MultiQueryAttention(nn.Module):
    def __init__(self, dim, num_q_heads, dropout=0.0):
        super().__init__()
        # 1. MQA 是 GQA 的特例：所有 query head 共享同一个 k/v head。
        assert dim % num_q_heads == 0
        self.dim = dim
        self.num_q_heads = num_q_heads
        self.head_dim = dim // num_q_heads
        self.q_proj = nn.Linear(dim, num_q_heads * self.head_dim)
        self.k_proj = nn.Linear(dim, self.head_dim)
        self.v_proj = nn.Linear(dim, self.head_dim)
        self.out = nn.Linear(dim, dim)
        self.dropout = dropout

    def forward(self, x, attn_mask=None, is_causal=False):
        B, T, _ = x.shape

        # 2. q 拆成多个头，k/v 只生成 1 个头。
        q = self.q_proj(x).view(B, T, self.num_q_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(x).view(B, T, 1, self.head_dim).transpose(1, 2)
        v = self.v_proj(x).view(B, T, 1, self.head_dim).transpose(1, 2)

        # 3. expand 不真实复制数据，只广播成每个 q head 都能访问同一份 k/v。
        k = k.expand(B, self.num_q_heads, T, self.head_dim)
        v = v.expand(B, self.num_q_heads, T, self.head_dim)

        # 4. 后续就是标准 scaled dot-product attention。
        scores = q @ k.transpose(-2, -1) / math.sqrt(self.head_dim)
        if is_causal:
            causal = torch.ones(T, T, dtype=torch.bool, device=x.device).tril()
            scores = scores.masked_fill(~causal, torch.finfo(scores.dtype).min)
        if attn_mask is not None:
            scores = scores.masked_fill(~attn_mask, torch.finfo(scores.dtype).min)
        attn = torch.softmax(scores, dim=-1)
        if self.dropout > 0.0 and self.training:
            attn = torch.dropout(attn, self.dropout, train=True)
        y = attn @ v

        # 5. 拼回 [B, T, dim] 后做输出投影。
        y = y.transpose(1, 2).contiguous().view(B, T, self.dim)
        return self.out(y)


if __name__ == "__main__":
    print(MultiQueryAttention(32, 4)(torch.randn(2, 5, 32)).shape)
