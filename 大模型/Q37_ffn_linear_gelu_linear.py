import torch.nn as nn


class FFN(nn.Module):
    def __init__(self, dim, hidden_dim, dropout=0.0):
        super().__init__()
        # 1. Transformer FFN: Linear 扩维 -> GELU 非线性 -> Dropout -> Linear 降维。
        self.net = nn.Sequential(nn.Linear(dim, hidden_dim), nn.GELU(), nn.Dropout(dropout), nn.Linear(hidden_dim, dim))

    def forward(self, x):
        # 2. FFN 对每个 token 独立作用，不混合序列位置。
        return self.net(x)
