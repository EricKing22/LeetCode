import torch


def bce_with_logits_loss(logits, target, reduction="mean"):
    # 1. 稳定版 BCEWithLogits：
    # max(x,0) - x*y + log(1 + exp(-abs(x)))，避免 sigmoid 后再取 log。
    loss = torch.clamp(logits, min=0) - logits * target + torch.log1p(torch.exp(-logits.abs()))

    # 2. 按 reduction 返回标量或逐元素 loss。
    if reduction == "mean":
        return loss.mean()
    if reduction == "sum":
        return loss.sum()
    return loss


if __name__ == "__main__":
    logits = torch.randn(4)
    target = torch.tensor([1.0, 0.0, 1.0, 0.0])
    print(bce_with_logits_loss(logits, target))
