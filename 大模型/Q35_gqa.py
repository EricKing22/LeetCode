import math

import torch
import torch.nn as nn


class GroupedQueryAttention(nn.Module):
    def __init__(self, dim, num_q_heads, num_kv_heads, dropout=0.0):
        super().__init__()
        # 1. GQA 要求多个 query head 共享一组 key/value head。
        assert num_q_heads % num_kv_heads == 0
        assert dim % num_q_heads == 0
        self.dim = dim
        self.num_q_heads = num_q_heads
        self.num_kv_heads = num_kv_heads
        self.head_dim = dim // num_q_heads
        self.q_proj = nn.Linear(dim, num_q_heads * self.head_dim)
        self.k_proj = nn.Linear(dim, num_kv_heads * self.head_dim)
        self.v_proj = nn.Linear(dim, num_kv_heads * self.head_dim)
        self.out = nn.Linear(dim, dim)
        self.dropout = dropout

    def forward(self, x, attn_mask=None, is_causal=False):
        B, T, _ = x.shape

        # 2. q 有 num_q_heads 个头，k/v 只有 num_kv_heads 个头。
        q = self.q_proj(x).view(B, T, self.num_q_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(x).view(B, T, self.num_kv_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(x).view(B, T, self.num_kv_heads, self.head_dim).transpose(1, 2)

        # 3. 将 k/v 按组复制到 query head 数量，达到共享 KV 的效果。
        repeat = self.num_q_heads // self.num_kv_heads
        k = k.repeat_interleave(repeat, dim=1)
        v = v.repeat_interleave(repeat, dim=1)

        # 4. 后续计算和普通多头注意力一致。
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

        # 5. 多个 query head 拼回模型维度。
        y = y.transpose(1, 2).contiguous().view(B, T, self.dim)
        return self.out(y)
