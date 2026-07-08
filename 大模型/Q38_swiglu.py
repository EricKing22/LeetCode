import torch
import torch.nn as nn


class SwiGLU(nn.Module):
    def __init__(self, dim, hidden_dim):
        super().__init__()
        # 1. SwiGLU 使用两条输入投影分支：一条做门控，一条保留内容。
        self.w1 = nn.Linear(dim, hidden_dim, bias=False)
        self.w2 = nn.Linear(dim, hidden_dim, bias=False)
        self.w3 = nn.Linear(hidden_dim, dim, bias=False)

    def forward(self, x):
        # 2. silu(w1(x)) 是门控值，乘上 w2(x) 后再投影回原维度。
        return self.w3(torch.nn.functional.silu(self.w1(x)) * self.w2(x))
