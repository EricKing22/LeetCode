import math

import torch


def scaled_dot_product_attention(q, k, v, attn_mask=None, dropout_p=0.0, training=True, is_causal=False):
    # 1. 注意力分数：QK^T / sqrt(d)，缩放可以避免维度变大后 logits 过大。
    d = q.size(-1)
    scores = q @ k.transpose(-2, -1) / math.sqrt(d)

    # 2. causal mask 保证当前位置只能看见自己和之前的 token。
    if is_causal:
        L, S = q.size(-2), k.size(-2)
        causal = torch.ones(L, S, dtype=torch.bool, device=q.device).tril()
        scores = scores.masked_fill(~causal, torch.finfo(scores.dtype).min)

    # 3. 支持布尔 mask 和加性 mask 两种常见形式。
    if attn_mask is not None:
        if attn_mask.dtype == torch.bool:
            scores = scores.masked_fill(~attn_mask, torch.finfo(scores.dtype).min)
        else:
            scores = scores + attn_mask

    # 4. softmax 得到注意力权重，再可选 dropout。
    attn = torch.softmax(scores, dim=-1)
    if dropout_p > 0.0 and training:
        attn = torch.dropout(attn, dropout_p, train=True)

    # 5. 输出是注意力权重对 V 的加权和，同时返回 attn 便于调试。
    return attn @ v, attn


if __name__ == "__main__":
    q = k = v = torch.randn(2, 4, 8, 16)
    print(scaled_dot_product_attention(q, k, v, is_causal=True)[0].shape)
