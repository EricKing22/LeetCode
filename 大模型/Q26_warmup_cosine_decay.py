import math


def warmup_cosine_lr(step, max_steps, base_lr, warmup_steps=0, min_lr=0.0):
    # 1. warmup 阶段线性升高学习率，避免训练初期不稳定。
    if warmup_steps > 0 and step < warmup_steps:
        return base_lr * float(step + 1) / warmup_steps

    # 2. warmup 后把进度映射到 [0, 1]。
    progress = (step - warmup_steps) / max(1, max_steps - warmup_steps)
    progress = min(max(progress, 0.0), 1.0)

    # 3. 使用半个 cosine 曲线从 base_lr 衰减到 min_lr。
    cosine = 0.5 * (1.0 + math.cos(math.pi * progress))
    return min_lr + (base_lr - min_lr) * cosine


if __name__ == "__main__":
    print([round(warmup_cosine_lr(i, 10, 1e-3, 2), 6) for i in range(4)])
