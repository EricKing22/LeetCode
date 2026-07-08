import torch


def dropout(x, p=0.5, training=True):
    # 1. 推理阶段不随机丢弃，直接返回原输入。
    if not training or p == 0.0:
        return x
    if p >= 1.0:
        # 2. p=1 表示所有神经元都被丢弃。
        return torch.zeros_like(x)

    # 3. 训练阶段采样保留 mask，并除以 1-p 保持期望不变。
    mask = (torch.rand_like(x) > p).to(x.dtype)
    return x * mask / (1.0 - p)


if __name__ == "__main__":
    x = torch.ones(10)
    print(dropout(x, p=0.5, training=True))
    print(dropout(x, p=0.5, training=False))
