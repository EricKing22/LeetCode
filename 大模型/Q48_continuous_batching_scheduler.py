from dataclasses import dataclass, field

import torch


class KVCache:
    def __init__(self):
        # 1. 每个请求可以维护自己的 per-layer KV cache。
        self.cache = {}

    def append(self, layer_idx, key, value):
        # 2. 首次生成该层 cache 时直接保存。
        old = self.cache.get(layer_idx)
        if old is None:
            self.cache[layer_idx] = (key, value)
        else:
            # 3. 解码阶段每步追加一个 token 的 key/value。
            old_k, old_v = old
            self.cache[layer_idx] = (torch.cat([old_k, key], dim=-2), torch.cat([old_v, value], dim=-2))
        return self.cache[layer_idx]


def _next_logits(model_out):
    # 1. 统一不同模型输出格式，最终取出 logits。
    if isinstance(model_out, tuple):
        model_out = model_out[0]
    if hasattr(model_out, "logits"):
        model_out = model_out.logits
    return model_out[:, -1, :]


@dataclass
class DecodeRequest:
    # 1. 一个 DecodeRequest 表示一条正在生成或等待生成的请求。
    request_id: str
    input_ids: torch.Tensor
    max_new_tokens: int
    generated: int = 0
    finished: bool = False
    cache: KVCache = field(default_factory=KVCache)


class ContinuousBatchScheduler:
    def __init__(self, model, max_batch_size=8, eos_id=None):
        # 1. waiting 存新请求，running 存当前正在一起解码的请求。
        self.model = model
        self.max_batch_size = max_batch_size
        self.eos_id = eos_id
        self.waiting = []
        self.running = []

    def add_request(self, req):
        # 2. 新请求先进入等待队列，后续 step 再加入运行批次。
        self.waiting.append(req)

    @torch.no_grad()
    def step(self):
        # 3. 只要 running 还有容量，就从 waiting 补请求进来。
        while self.waiting and len(self.running) < self.max_batch_size:
            self.running.append(self.waiting.pop(0))
        if not self.running:
            return []

        # 4. 连续批处理每次只取每个请求最后一个 token 做下一步解码。
        input_ids = torch.cat([r.input_ids[:, -1:] for r in self.running], dim=0)
        logits = _next_logits(self.model(input_ids))
        next_ids = logits.argmax(dim=-1, keepdim=True)

        # 5. 把新 token 追加回各自请求，并按是否完成拆分队列。
        finished = []
        still_running = []
        for req, token in zip(self.running, next_ids):
            req.input_ids = torch.cat([req.input_ids, token.view(1, 1)], dim=-1)
            req.generated += 1
            req.finished = req.generated >= req.max_new_tokens or (self.eos_id is not None and int(token) == self.eos_id)
            (finished if req.finished else still_running).append(req)
        self.running = still_running

        # 6. 返回本 step 完成的请求，调用方可以取走结果。
        return finished
