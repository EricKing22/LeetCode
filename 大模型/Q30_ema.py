import torch


class EMA:
    def __init__(self, model, decay=0.999):
        # 1. shadow 保存模型浮点参数/缓冲区的指数滑动平均副本。
        self.decay = decay
        self.shadow = {k: v.detach().clone() for k, v in model.state_dict().items() if v.dtype.is_floating_point}

    @torch.no_grad()
    def update(self, model):
        # 2. 每次训练更新后调用：shadow = decay * shadow + (1-decay) * current。
        for k, v in model.state_dict().items():
            if k in self.shadow:
                self.shadow[k].mul_(self.decay).add_(v.detach(), alpha=1 - self.decay)

    def copy_to(self, model):
        # 3. 推理或评估前，把 EMA 权重拷贝到模型里。
        state = model.state_dict()
        for k, v in self.shadow.items():
            state[k].copy_(v)
