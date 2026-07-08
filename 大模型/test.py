
import torch
def sinusoidal_position_encoding(seq_len, dim, base=10000):
    pos = torch.arange(dim).unsqueeze(-1)
    inv_freq = 1 / ( base ** (torch.arange(0,dim,2) / dim))

    emb = pos * inv_freq

    pe = torch.zeros(seq_len, dim)
    pe[:, 0::2] = torch.sin(emb)
    pe[:, 1::2] = torch.cos(emb)

    return pe