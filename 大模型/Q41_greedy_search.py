import torch


def _next_logits(model_out):
    # 1. 兼容不同模型输出：tuple、带 logits 属性的对象，或直接 logits Tensor。
    if isinstance(model_out, tuple):
        model_out = model_out[0]
    if hasattr(model_out, "logits"):
        model_out = model_out.logits

    # 2. 只取最后一个位置的 logits，用来预测下一个 token。
    return model_out[:, -1, :]


@torch.no_grad()
def greedy_search(model, input_ids, max_new_tokens, eos_id=None):
    # 1. 贪心搜索每一步都选择概率最大的 token。
    for _ in range(max_new_tokens):
        logits = _next_logits(model(input_ids))
        next_id = logits.argmax(dim=-1, keepdim=True)
        input_ids = torch.cat([input_ids, next_id], dim=-1)

        # 2. 如果所有样本都生成 eos，则提前停止。
        if eos_id is not None and bool((next_id == eos_id).all()):
            break
    return input_ids
