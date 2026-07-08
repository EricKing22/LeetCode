import math

import torch
import torch.nn as nn


def scaled_dot_product_attention(q, k, v, attn_mask=None, is_causal=False):
    # 1. 单头注意力的核心：scores = QK^T / sqrt(d)。
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))

    # 2. causal mask 用于解码任务，防止看见未来 token。
    if is_causal:
        L, S = q.size(-2), k.size(-2)
        causal = torch.ones(L, S, dtype=torch.bool, device=q.device).tril()
        scores = scores.masked_fill(~causal, torch.finfo(scores.dtype).min)

    # 3. 外部 mask 常用于 padding mask。
    if attn_mask is not None:
        scores = scores.masked_fill(~attn_mask, torch.finfo(scores.dtype).min)

    # 4. softmax 后乘 V，得到上下文向量。
    return torch.softmax(scores, dim=-1) @ v


class SingleHeadSelfAttention(nn.Module):
    def __init__(self, dim):
        super().__init__()
        # 1. 一次线性投影同时生成 q/k/v，最后再用 out 投影回原维度。
        self.qkv = nn.Linear(dim, 3 * dim)
        self.out = nn.Linear(dim, dim)

    def forward(self, x, attn_mask=None, is_causal=False):
        # 2. chunk 把最后一维拆成 q、k、v 三份。
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        return self.out(scaled_dot_product_attention(q, k, v, attn_mask, is_causal))


if __name__ == "__main__":
    print(SingleHeadSelfAttention(32)(torch.randn(2, 5, 32)).shape)
