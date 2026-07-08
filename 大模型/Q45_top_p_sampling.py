import torch


def temperature_sample(logits, temperature=1.0):
    # 1. temperature <= 0 时退化为 argmax。
    if temperature <= 0:
        return logits.argmax(dim=-1)
    prob = torch.softmax(logits / temperature, dim=-1)
    return torch.multinomial(prob, num_samples=1).squeeze(-1)


def top_p_sample(logits, p=0.9, temperature=1.0):
    # 1. 先按 logits 从大到小排序，方便累计概率。
    sorted_logits, sorted_idx = torch.sort(logits, descending=True, dim=-1)
    prob = torch.softmax(sorted_logits / max(temperature, 1e-8), dim=-1)
    cum_prob = prob.cumsum(dim=-1)

    # 2. 删除累计概率超过 p 之后的 token，但至少保留第一个 token。
    remove = cum_prob > p
    remove[..., 1:] = remove[..., :-1].clone()
    remove[..., 0] = False

    # 3. 被移除的 token logits 置为极小值，相当于采样概率为 0。
    sorted_logits = sorted_logits.masked_fill(remove, torch.finfo(logits.dtype).min)
    chosen = temperature_sample(sorted_logits, temperature=temperature)

    # 4. chosen 是排序后下标，需要 gather 回原词表 token id。
    return sorted_idx.gather(-1, chosen.unsqueeze(-1)).squeeze(-1)
