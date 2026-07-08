import torch


@torch.no_grad()
def clip_grad_global_norm(parameters, max_norm, eps=1e-6):
    # 1. 只处理已经有梯度的参数。
    params = [p for p in parameters if p.grad is not None]
    if not params:
        return torch.tensor(0.0)
    device = params[0].device

    # 2. global norm = sqrt(sum_i ||grad_i||_2^2)。
    total_norm = torch.norm(torch.stack([p.grad.detach().norm(2).to(device) for p in params]), 2)

    # 3. 如果总范数超过 max_norm，就按比例缩小；否则 scale=1。
    scale = (max_norm / (total_norm + eps)).clamp(max=1.0)
    for p in params:
        p.grad.mul_(scale)
    return total_norm
