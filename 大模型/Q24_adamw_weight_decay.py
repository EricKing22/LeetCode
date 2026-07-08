import torch


class AdamW:
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=1e-2):
        # 1. AdamW 与 Adam 一样维护一阶矩 m 和二阶矩 v。
        self.params = list(params)
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.weight_decay = weight_decay
        self.t = 0
        self.m = [torch.zeros_like(p) for p in self.params]
        self.v = [torch.zeros_like(p) for p in self.params]

    @torch.no_grad()
    def step(self):
        self.t += 1
        for p, m, v in zip(self.params, self.m, self.v):
            if p.grad is None:
                continue

            # 2. AdamW 的关键：weight decay 与梯度更新解耦，先直接缩放参数。
            p.mul_(1 - self.lr * self.weight_decay)
            g = p.grad

            # 3. 更新 Adam 的一阶矩和二阶矩。
            m.mul_(self.beta1).add_(g, alpha=1 - self.beta1)
            v.mul_(self.beta2).addcmul_(g, g, value=1 - self.beta2)

            # 4. 做 bias correction 后更新参数。
            m_hat = m / (1 - self.beta1 ** self.t)
            v_hat = v / (1 - self.beta2 ** self.t)
            p.addcdiv_(m_hat, v_hat.sqrt().add(self.eps), value=-self.lr)

    def zero_grad(self):
        # 5. 梯度清空，优化器的历史状态继续保留。
        for p in self.params:
            p.grad = None
