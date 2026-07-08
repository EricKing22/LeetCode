import torch
import torch.nn as nn


class CustomLayerNorm(nn.Module):
    def __init__(self, normalized_shape, eps=1e-5, elementwise_affine=True):
        super().__init__()
        # 1. normalized_shape 表示最后几个维度一起做 LayerNorm。
        if isinstance(normalized_shape, int):
            normalized_shape = (normalized_shape,)
        self.normalized_shape = tuple(normalized_shape)
        self.eps = eps
        self.elementwise_affine = elementwise_affine
        if elementwise_affine:
            # 2. weight/bias 的形状和被归一化的尾部维度一致。
            self.weight = nn.Parameter(torch.ones(self.normalized_shape))
            self.bias = nn.Parameter(torch.zeros(self.normalized_shape))
        else:
            self.register_parameter("weight", None)
            self.register_parameter("bias", None)

    def forward(self, x):
        # 3. LayerNorm 对每个样本内部的最后若干维求均值和方差。
        dims = tuple(range(x.dim() - len(self.normalized_shape), x.dim()))
        mean = x.mean(dim=dims, keepdim=True)
        var = x.var(dim=dims, unbiased=False, keepdim=True)

        # 4. 标准化后再做逐元素 affine。
        y = (x - mean) / torch.sqrt(var + self.eps)
        if self.elementwise_affine:
            y = y * self.weight + self.bias
        return y


if __name__ == "__main__":
    x = torch.randn(2, 3, 4)
    print(CustomLayerNorm(4)(x).shape)
