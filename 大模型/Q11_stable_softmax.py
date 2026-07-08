import torch


def stable_softmax(x, dim=-1):
    # 1. softmax(x) 与 softmax(x - max(x)) 等价，但后者能避免 exp 溢出。
    x = x - x.max(dim=dim, keepdim=True).values
    exp_x = torch.exp(x)

    # 2. 在指定维度上归一化，得到概率分布。
    return exp_x / exp_x.sum(dim=dim, keepdim=True)


if __name__ == "__main__":
    x = torch.tensor([[1000.0, 1001.0]])
    print(stable_softmax(x))
