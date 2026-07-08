import torch


def temperature_sample(logits, temperature=1.0):
    # 1. temperature <= 0 时退化成贪心选择。
    if temperature <= 0:
        return logits.argmax(dim=-1)

    # 2. temperature 越大分布越平，越小越接近 argmax。
    prob = torch.softmax(logits / temperature, dim=-1)

    # 3. 从概率分布中采样一个 token。
    return torch.multinomial(prob, num_samples=1).squeeze(-1)
