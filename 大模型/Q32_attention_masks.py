import torch


def make_padding_mask(input_ids, pad_id=0):
    # 1. True 表示可见 token，False 表示 padding，需要在 attention 中屏蔽。
    return (input_ids != pad_id)[:, None, None, :]


def make_causal_mask(seq_len, device=None):
    # 1. 下三角矩阵表示自回归可见范围：第 i 行只能看 <= i 的位置。
    return torch.ones(seq_len, seq_len, dtype=torch.bool, device=device).tril()[None, None, :, :]


if __name__ == "__main__":
    ids = torch.tensor([[1, 2, 0], [3, 0, 0]])
    print(make_padding_mask(ids).shape)
    print(make_causal_mask(3))
