import torch


def temperature_sample(logits, temperature=1.0):
    # 1. temperature <= 0 时不采样，直接取最大 logits。
    if temperature <= 0:
        return logits.argmax(dim=-1)
    prob = torch.softmax(logits / temperature, dim=-1)
    return torch.multinomial(prob, num_samples=1).squeeze(-1)


def top_k_sample(logits, k=50, temperature=1.0):
    # 1. k 不能超过词表大小。
    k = min(k, logits.size(-1))

    # 2. 只保留 logits 最高的 k 个 token，在这个子集里采样。
    values, indices = torch.topk(logits, k, dim=-1)
    next_in_topk = temperature_sample(values, temperature)

    # 3. next_in_topk 是 top-k 子集内下标，需要映射回原词表下标。
    return indices.gather(-1, next_in_topk.unsqueeze(-1)).squeeze(-1)
