import torch


class Momentum:
    def __init__(self, params, lr=1e-3, momentum=0.9):
        # 1. velocity 为每个参数保存历史梯度的指数累积。
        self.params = list(params)
        self.lr = lr
        self.momentum = momentum
        self.velocity = [torch.zeros_like(p) for p in self.params]

    @torch.no_grad()
    def step(self):
        for p, v in zip(self.params, self.velocity):
            if p.grad is None:
                continue
            # 2. 动量更新：v = momentum * v + grad。
            v.mul_(self.momentum).add_(p.grad)

            # 3. 参数沿动量方向更新。
            p.add_(v, alpha=-self.lr)

    def zero_grad(self):
        # 4. 清空梯度，保留 velocity 作为跨 step 的状态。
        for p in self.params:
            p.grad = None
