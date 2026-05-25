import torch
import torch.nn as nn

class BatchNorm(nn.Module):
    def __init__(self, num_features, training, momentum = 0.1, eps = 1e-5):
        super().__init__()
        self.momentum = momentum
        self.eps = eps

        self.gamma = nn.Parameter(torch.ones(num_features))
        self.beta = nn.Parameter(torch.zeros(num_features))

        self.register_buffer("running_mean", torch.zeros(num_features))
        self.register_buffer("running_var", torch.ones(num_features))
        self.training = training

    def forward(self, x):

        if self.training:

            batch_mean = x.mean(dim=-1)
            batch_var = x.var(dim=-1)

            with torch.no_grad:
                self.running_mean = self.momentum * batch_mean + (1 - self.momentum) * self.running_mean
                self.running_var = self.momentum * batch_var + (1 - self.momentum) * self.running_var

            mean = self.running_mean
            var = self.running_var

        else:
            mean = x.mean(dim=-1)
            var = x.var(dim=-1)

        normalized_x = (x-mean) / torch.sqrt(var + self.eps)

        return self.gamma * normalized_x + self.beta