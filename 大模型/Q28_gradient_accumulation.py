def train_one_epoch_with_accumulation(model, dataloader, optimizer, loss_fn, accum_steps=4, device="cpu"):
    # 1. 梯度累积用多个小 batch 模拟一个大 batch。
    model.train()
    optimizer.zero_grad()
    total_loss = 0.0
    for step, (x, y) in enumerate(dataloader, start=1):
        x, y = x.to(device), y.to(device)

        # 2. loss 除以 accum_steps，保证累积后的梯度尺度和大 batch 一致。
        loss = loss_fn(model(x), y) / accum_steps
        loss.backward()
        total_loss += float(loss.detach()) * accum_steps

        # 3. 每累积 accum_steps 次 backward，才真正更新一次参数。
        if step % accum_steps == 0:
            optimizer.step()
            optimizer.zero_grad()

    # 4. 如果最后剩余 batch 数不足 accum_steps，也要补一次更新。
    if len(dataloader) % accum_steps != 0:
        optimizer.step()
        optimizer.zero_grad()
    return total_loss / len(dataloader)
