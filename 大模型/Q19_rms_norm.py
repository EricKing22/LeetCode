import torch
import torch.nn as nn


class RMSNorm(nn.Module):
    def __init__(self, dim, eps=1e-6):
        super().__init__()
        # 1. RMSNorm 只缩放不平移，常用于 LLaMA 系列结构。
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x):
        # 2. 用均方根的倒数归一化：x / sqrt(mean(x^2) + eps)。
        rms = torch.rsqrt(x.pow(2).mean(dim=-1, keepdim=True) + self.eps)
        return x * rms * self.weight


if __name__ == "__main__":
    x = torch.randn(2, 3, 4)
    print(RMSNorm(4)(x).shape)
