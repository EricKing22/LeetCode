import torch

from Q17_batch_norm_1d import CustomBatchNorm1d


# Q17: BatchNorm1d forward.
if __name__ == "__main__":
    torch.manual_seed(0)
    x = torch.randn(20, 10)
    bn = CustomBatchNorm1d(10)
    y = bn(x)
    print("output shape:", y.shape)
    print("running_mean shape:", bn.running_mean.shape)
