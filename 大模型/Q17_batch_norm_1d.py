import torch
import torch.nn as nn


class CustomBatchNorm1d(nn.Module):
    def __init__(self, num_features, eps=1e-5, momentum=0.1, affine=True):
        super().__init__()
        # 1. eps 防止除零，momentum 控制 running statistics 的更新速度。
        self.eps = eps
        self.momentum = momentum
        self.affine = affine
        if affine:
            # 2. affine=True 时学习 gamma/beta，恢复表达能力。
            self.weight = nn.Parameter(torch.ones(num_features))
            self.bias = nn.Parameter(torch.zeros(num_features))
        else:
            self.register_parameter("weight", None)
            self.register_parameter("bias", None)
        self.register_buffer("running_mean", torch.zeros(num_features))
        self.register_buffer("running_var", torch.ones(num_features))

    def forward(self, x):
        # 3. 兼容 [N, C] 和 [N, C, L]：BatchNorm 在 batch/长度维度上统计。
        dims = (0,) if x.dim() == 2 else (0, 2)
        shape = (1, -1) if x.dim() == 2 else (1, -1, 1)
        if self.training:
            # 4. 训练阶段使用当前 batch 的均值和方差归一化。
            mean = x.mean(dim=dims, keepdim=True)
            var = x.var(dim=dims, unbiased=False, keepdim=True)
            with torch.no_grad():
                # 5. running_var 使用无偏估计，模拟 PyTorch BatchNorm 的习惯。
                self.running_mean.mul_(1 - self.momentum).add_(self.momentum * mean.reshape(-1))
                unbiased_var = x.var(dim=dims, unbiased=True).reshape(-1)
                self.running_var.mul_(1 - self.momentum).add_(self.momentum * unbiased_var)
        else:
            # 6. 推理阶段使用训练期间累计的 running mean/var。
            mean = self.running_mean.reshape(shape)
            var = self.running_var.reshape(shape)

        # 7. 标准化后可选地做 gamma/beta 仿射变换。
        y = (x - mean) / torch.sqrt(var + self.eps)
        if self.affine:
            y = y * self.weight.reshape(shape) + self.bias.reshape(shape)
        return y


if __name__ == "__main__":
    x = torch.randn(20, 10)
    print(CustomBatchNorm1d(10)(x).shape)
