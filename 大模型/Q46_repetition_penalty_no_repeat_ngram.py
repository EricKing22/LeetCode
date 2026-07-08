import torch


def apply_repetition_penalty(logits, generated_ids, penalty=1.1):
    # 1. clone 避免原地修改调用方传入的 logits。
    logits = logits.clone()
    for token in set(generated_ids.reshape(-1).tolist()):
        # 2. 对已生成 token 降低其再次出现的倾向；正负 logit 分开处理保持惩罚方向一致。
        score = logits[..., token]
        logits[..., token] = torch.where(score < 0, score * penalty, score / penalty)
    return logits


def banned_ngram_tokens(generated_ids, ngram_size):
    # 1. 如果长度还不足以形成 n-gram，就没有需要禁用的 token。
    if ngram_size <= 0 or len(generated_ids) + 1 < ngram_size:
        return set()

    # 2. 当前前缀是最后 n-1 个 token，寻找历史中同样前缀后面接过的 token。
    prefix = tuple(generated_ids[-(ngram_size - 1):])
    banned = set()
    for i in range(len(generated_ids) - ngram_size + 1):
        ngram = tuple(generated_ids[i:i + ngram_size])
        if ngram[:-1] == prefix:
            banned.add(ngram[-1])
    return banned


def apply_no_repeat_ngram(logits, generated_ids, ngram_size):
    # 1. 将会造成重复 n-gram 的 token 置为极小值，使其无法被采样。
    logits = logits.clone()
    for token in banned_ngram_tokens(generated_ids, ngram_size):
        logits[..., token] = torch.finfo(logits.dtype).min
    return logits
