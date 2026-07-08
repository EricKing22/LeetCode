import torch


def cross_entropy_from_logits(logits, target, reduction="mean"):
    # 1. log_softmax = logits - logsumexp(logits)，比先 softmax 再 log 稳定。
    log_prob = logits - torch.logsumexp(logits, dim=-1, keepdim=True)

    # 2. gather 取出每个样本真实类别对应的 log probability。
    loss = -log_prob.gather(dim=-1, index=target.unsqueeze(-1)).squeeze(-1)

    # 3. 按 reduction 返回均值、求和或逐样本 loss。
    if reduction == "mean":
        return loss.mean()
    if reduction == "sum":
        return loss.sum()
    return loss


if __name__ == "__main__":
    logits = torch.randn(3, 5)
    target = torch.tensor([1, 2, 3])
    print(cross_entropy_from_logits(logits, target))
