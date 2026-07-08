import torch


class SGD:
    def __init__(self, params, lr=1e-3, weight_decay=0.0):
        # 1. 保存要优化的参数列表和超参数。
        self.params = list(params)
        self.lr = lr
        self.weight_decay = weight_decay

    @torch.no_grad()
    def step(self):
        # 2. 参数更新不需要记录梯度图，所以用 no_grad。
        for p in self.params:
            if p.grad is None:
                continue
            g = p.grad
            if self.weight_decay:
                # 3. 这里是 L2 weight decay：梯度中加 lambda * w。
                g = g + self.weight_decay * p
            # 4. SGD 更新：p = p - lr * grad。
            p.add_(g, alpha=-self.lr)

    def zero_grad(self):
        # 5. 将梯度置 None，下一轮 backward 会重新分配梯度。
        for p in self.params:
            p.grad = None
