import torch
import torch.nn as nn

from LayerNorm import CustomLayerNorm


def test_layer_norm_matches_torch():
    torch.manual_seed(0)
    x = torch.randn(2, 3, 4)
    custom = CustomLayerNorm(4)
    official = nn.LayerNorm(4)
    with torch.no_grad():
        official.weight.copy_(custom.weight)
        official.bias.copy_(custom.bias)
    diff = (custom(x) - official(x)).abs().max().item()
    assert diff < 1e-5, diff


if __name__ == "__main__":
    test_layer_norm_matches_torch()
    print("LayerNorm test passed")
