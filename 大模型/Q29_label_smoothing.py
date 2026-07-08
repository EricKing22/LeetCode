import torch


def label_smoothing_loss(logits, target, smoothing=0.1, reduction="mean"):
    # 1. logits 最后一维是类别数。
    n_classes = logits.size(-1)
    log_prob = torch.log_softmax(logits, dim=-1)

    # 2. 构造平滑后的目标分布：真实类不是 1，而是 1-smoothing+smoothing/C。
    with torch.no_grad():
        true_dist = torch.full_like(log_prob, smoothing / n_classes)
        true_dist.scatter_(1, target.unsqueeze(1), 1.0 - smoothing + smoothing / n_classes)

    # 3. 对平滑目标分布和预测 log_prob 做交叉熵。
    loss = -(true_dist * log_prob).sum(dim=-1)
    if reduction == "sum":
        return loss.sum()
    if reduction == "none":
        return loss
    return loss.mean()


if __name__ == "__main__":
    print(label_smoothing_loss(torch.randn(2, 5), torch.tensor([1, 2])))
