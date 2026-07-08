import torch

from Q18_layer_norm import CustomLayerNorm


# Q18: LayerNorm forward.
if __name__ == "__main__":
    torch.manual_seed(0)
    x = torch.randn(2, 3, 4)
    ln = CustomLayerNorm(4)
    y = ln(x)
    print("output shape:", y.shape)
