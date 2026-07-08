import torch

from Q34_multi_head_attention import MultiHeadAttention, scaled_dot_product_attention


# Q31/Q34: Scaled dot-product attention and Multi-Head Attention.
if __name__ == "__main__":
    torch.manual_seed(0)
    x = torch.randn(2, 10, 256)
    mha = MultiHeadAttention(dim=256, num_heads=8, dropout=0.0)
    y = mha(x, is_causal=True)
    print("output shape:", y.shape)
