import math

import torch
import torch.nn as nn


def scaled_dot_product_attention(q, k, v, attn_mask=None, dropout_p=0.0, training=True, is_causal=False):
    # 1. 多头版本中 q/k/v 通常是 [B, H, T, D_head]。
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
    if is_causal:
        # 2. causal mask 会自动广播到 batch 和 head 维度。
        L, S = q.size(-2), k.size(-2)
        causal = torch.ones(L, S, dtype=torch.bool, device=q.device).tril()
        scores = scores.masked_fill(~causal, torch.finfo(scores.dtype).min)
    if attn_mask is not None:
        if attn_mask.dtype == torch.bool:
            scores = scores.masked_fill(~attn_mask, torch.finfo(scores.dtype).min)
        else:
            scores = scores + attn_mask

    # 3. 注意力权重可选 dropout，训练时使用。
    attn = torch.softmax(scores, dim=-1)
    if dropout_p > 0.0 and training:
        attn = torch.dropout(attn, dropout_p, train=True)
    return attn @ v


class MultiHeadAttention(nn.Module):
    def __init__(self, dim, num_heads, dropout=0.0):
        super().__init__()
        # 1. dim 必须能整除 head 数，才能均分到每个 head。
        assert dim % num_heads == 0
        self.dim = dim
        self.num_heads = num_heads
        self.head_dim = dim // num_heads
        self.qkv = nn.Linear(dim, 3 * dim)
        self.out = nn.Linear(dim, dim)
        self.dropout = dropout

    def _split_heads(self, x):
        # 2. [B, T, D] -> [B, H, T, D_head]，方便并行计算每个 head。
        B, T, _ = x.shape
        return x.view(B, T, self.num_heads, self.head_dim).transpose(1, 2)

    def forward(self, x, attn_mask=None, is_causal=False):
        # 3. 先生成 q/k/v，再拆成多个 head。
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        q, k, v = self._split_heads(q), self._split_heads(k), self._split_heads(v)
        y = scaled_dot_product_attention(q, k, v, attn_mask, self.dropout, self.training, is_causal)

        # 4. 把多个 head 拼回 [B, T, D]，再输出投影。
        y = y.transpose(1, 2).contiguous().view(x.size(0), x.size(1), self.dim)
        return self.out(y)


if __name__ == "__main__":
    print(MultiHeadAttention(32, 4)(torch.randn(2, 5, 32), is_causal=True).shape)
