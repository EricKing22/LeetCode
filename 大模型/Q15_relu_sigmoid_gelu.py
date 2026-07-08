import math

import torch


def relu(x):
    # 1. ReLU: 小于 0 的位置截断为 0。
    return torch.maximum(x, torch.zeros_like(x))


def sigmoid(x):
    # 1. Sigmoid 把任意实数压到 (0, 1)。
    return 1.0 / (1.0 + torch.exp(-x))


def gelu(x):
    # 1. GELU 的 tanh 近似形式，Transformer FFN 中常用。
    return 0.5 * x * (1.0 + torch.tanh(math.sqrt(2.0 / math.pi) * (x + 0.044715 * x ** 3)))


if __name__ == "__main__":
    x = torch.linspace(-2, 2, 5)
    print(relu(x), sigmoid(x), gelu(x))
