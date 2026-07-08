import torch
import torch.nn as nn

from BatchNorm import CustomBatchNorm1d


def test_batch_norm_matches_torch():
    torch.manual_seed(0)
    x = torch.randn(16, 8)
    custom = CustomBatchNorm1d(8)
    official = nn.BatchNorm1d(8)
    with torch.no_grad():
        official.weight.copy_(custom.weight)
        official.bias.copy_(custom.bias)
    diff = (custom(x) - official(x)).abs().max().item()
    assert diff < 1e-5, diff


if __name__ == "__main__":
    test_batch_norm_matches_torch()
    print("BatchNorm test passed")
