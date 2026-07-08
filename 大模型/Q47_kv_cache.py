import torch


class KVCache:
    def __init__(self):
        # 1. cache 按 layer_idx 保存每层已经生成过的 key/value。
        self.cache = {}

    def append(self, layer_idx, key, value):
        # 2. 第一次写入该层时直接保存当前 key/value。
        old = self.cache.get(layer_idx)
        if old is None:
            self.cache[layer_idx] = (key, value)
        else:
            # 3. 后续解码时沿序列维 dim=-2 追加新 token 的 key/value。
            old_k, old_v = old
            self.cache[layer_idx] = (torch.cat([old_k, key], dim=-2), torch.cat([old_v, value], dim=-2))
        return self.cache[layer_idx]
