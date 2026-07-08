import torch


def _next_logits(model_out):
    # 1. 兼容常见模型输出格式，统一拿到 logits Tensor。
    if isinstance(model_out, tuple):
        model_out = model_out[0]
    if hasattr(model_out, "logits"):
        model_out = model_out.logits

    # 2. 只用最后一个 token 的分布预测下一个 token。
    return model_out[:, -1, :]


@torch.no_grad()
def beam_search(model, input_ids, max_new_tokens, beam_size=4, eos_id=None, length_penalty=0.7):
    # 1. 每个 beam 保存：(当前序列, 累计 log 概率, 是否结束)。
    beams = [(input_ids, 0.0, False)]
    for _ in range(max_new_tokens):
        candidates = []
        for ids, score, done in beams:
            if done:
                # 2. 已经生成 eos 的 beam 直接保留，不再扩展。
                candidates.append((ids, score, True))
                continue

            # 3. 对当前 beam 取 top beam_size 个候选 token 进行扩展。
            log_prob = torch.log_softmax(_next_logits(model(ids)), dim=-1)[0]
            top_score, top_id = torch.topk(log_prob, beam_size)
            for s, token in zip(top_score.tolist(), top_id.tolist()):
                new_ids = torch.cat([ids, ids.new_tensor([[token]])], dim=-1)
                candidates.append((new_ids, score + s, eos_id is not None and token == eos_id))

        def rank(item):
            # 4. length penalty 用来缓解 beam search 偏好短句的问题。
            ids, score, _ = item
            lp = ((5 + ids.size(1)) / 6) ** length_penalty
            return score / lp

        # 5. 从所有候选中保留排名最高的 beam_size 个。
        beams = sorted(candidates, key=rank, reverse=True)[:beam_size]
        if all(done for _, _, done in beams):
            break

    # 6. 返回最终 length-normalized score 最高的序列。
    return max(beams, key=lambda item: item[1] / (((5 + item[0].size(1)) / 6) ** length_penalty))[0]
