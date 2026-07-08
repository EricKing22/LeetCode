import torch


def mse_loss_and_backward(pred, target, reduction="mean"):
    # 1. MSE 的误差项 diff = pred - target。
    diff = pred - target
    if reduction == "sum":
        # 2. sum reduction: L = sum(diff^2)，梯度是 2 * diff。
        return (diff ** 2).sum(), 2.0 * diff

    # 3. mean reduction: 梯度还要除以元素总数。
    return (diff ** 2).mean(), 2.0 * diff / diff.numel()


if __name__ == "__main__":
    pred = torch.tensor([1.0, 2.0, 3.0])
    target = torch.tensor([1.0, 1.0, 1.0])
    print(mse_loss_and_backward(pred, target))
