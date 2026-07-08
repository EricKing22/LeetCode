import torch
import torch.nn as nn


class LoRALinear(nn.Module):
    def __init__(self, in_features, out_features, r=8, alpha=16, bias=True):
        super().__init__()
        # 1. base 是冻结的原始线性层，LoRA 只训练低秩增量。
        self.base = nn.Linear(in_features, out_features, bias=bias)
        for p in self.base.parameters():
            p.requires_grad = False

        # 2. 低秩分解增量：Delta W = A @ B，秩为 r。
        self.A = nn.Parameter(torch.randn(in_features, r) * 0.01)
        self.B = nn.Parameter(torch.zeros(r, out_features))
        self.scaling = alpha / r

    def forward(self, x):
        # 3. 输出 = 冻结基座输出 + 缩放后的 LoRA 增量输出。
        return self.base(x) + (x @ self.A @ self.B) * self.scaling
