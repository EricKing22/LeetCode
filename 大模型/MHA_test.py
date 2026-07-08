import torch

from MHA import MultiHeadAttention


def test_mha_shape():
    torch.manual_seed(0)
    x = torch.randn(2, 6, 32)
    mha = MultiHeadAttention(dim=32, num_heads=4)
    y = mha(x, is_causal=True)
    assert y.shape == x.shape


if __name__ == "__main__":
    test_mha_shape()
    print("MHA test passed")
