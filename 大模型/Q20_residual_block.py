import torch
import torch.nn as nn


class SimpleLayerNorm(nn.Module):
    def __init__(self, dim, eps=1e-5):
        super().__init__()
        # 1. 简化版 LayerNorm：只对最后一维做归一化。
        self.weight = nn.Parameter(torch.ones(dim))
        self.bias = nn.Parameter(torch.zeros(dim))
        self.eps = eps

    def forward(self, x):
        # 2. 计算最后一维的均值和方差，然后进行标准化。
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, unbiased=False, keepdim=True)
        return (x - mean) / torch.sqrt(var + self.eps) * self.weight + self.bias


class ResidualBlock(nn.Module):
    def __init__(self, fn, dim, dropout_p=0.0, norm_first=True):
        super().__init__()
        # 1. fn 是残差分支中的子层，例如 Attention 或 FFN。
        self.fn = fn
        self.norm = SimpleLayerNorm(dim)
        self.dropout = nn.Dropout(dropout_p)
        self.norm_first = norm_first

    def forward(self, x, *args, **kwargs):
        # 2. Pre-Norm: x + Dropout(fn(LN(x)))，深层 Transformer 更常用。
        if self.norm_first:
            return x + self.dropout(self.fn(self.norm(x), *args, **kwargs))

        # 3. Post-Norm: LN(x + Dropout(fn(x)))。
        return self.norm(x + self.dropout(self.fn(x, *args, **kwargs)))


if __name__ == "__main__":
    block = ResidualBlock(nn.Linear(4, 4), dim=4)
    print(block(torch.randn(2, 3, 4)).shape)
