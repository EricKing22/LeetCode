import torch


class Adam:
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8):
        # 1. Adam 同时维护一阶矩 m 和二阶矩 v。
        self.params = list(params)
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.t = 0
        self.m = [torch.zeros_like(p) for p in self.params]
        self.v = [torch.zeros_like(p) for p in self.params]

    @torch.no_grad()
    def step(self):
        # 2. t 用于 bias correction，修正初期 m/v 偏小的问题。
        self.t += 1
        for p, m, v in zip(self.params, self.m, self.v):
            if p.grad is None:
                continue
            g = p.grad

            # 3. 更新一阶矩和二阶矩的指数滑动平均。
            m.mul_(self.beta1).add_(g, alpha=1 - self.beta1)
            v.mul_(self.beta2).addcmul_(g, g, value=1 - self.beta2)

            # 4. 偏差修正后的 m_hat/v_hat。
            m_hat = m / (1 - self.beta1 ** self.t)
            v_hat = v / (1 - self.beta2 ** self.t)

            # 5. Adam 更新：p -= lr * m_hat / (sqrt(v_hat) + eps)。
            p.addcdiv_(m_hat, v_hat.sqrt().add(self.eps), value=-self.lr)

    def zero_grad(self):
        # 6. 清空梯度，但保留 m/v 优化器状态。
        for p in self.params:
            p.grad = None
