import torch
import torch.nn as nn

class LayerNorm(nn.Module):
    def __init__(self, normalize_shape, eps = 1e-5):
        super().__init__()
        if isinstance(normalize_shape, int):
            self.normalize_shape = (normalize_shape, )
        else:
            self.normalize_shape = tuple(normalize_shape)
        self.gamma = nn.Parameter(torch.ones(self.normalize_shape))
        self.beta = nn.Parameter(torch.zeros(self.normalize_shape))

        self.eps = eps

    def forward(self, x):

        dim_to_reduce = list( range(len(x)-len(self.normalize_shape), len(x)))
        mean = x.mean(dim=list( range(len(x) - len(self.normalize_shape),len(x))), keepdim=True)
        std = x.std(dim=list( range(len(x) - len(self.normalize_shape),len(x))), keepdim=True)

        res = x - mean / (std + self.eps)

        return self.gamma * res + self.beta