import torch


def sinusoidal_position_encoding(seq_len, dim, base=10000.0):
    # 1. pos: [S, 1]，每一行是一个位置编号。
    pos = torch.arange(seq_len).float().unsqueeze(1)

    # 2. inv_freq: [D/2]，每两个维度共用一个频率。
    inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float() / dim))

    # 3. freqs: [S, 1] * [D/2] -> [S, D/2]。
    freqs = pos * inv_freq

    # 4. 偶数维放 sin，奇数维放 cos。
    pe = torch.zeros(seq_len, dim)
    pe[:, 0::2] = torch.sin(freqs)
    pe[:, 1::2] = torch.cos(freqs)
    return pe


if __name__ == "__main__":
    print(sinusoidal_position_encoding(4, 8))
