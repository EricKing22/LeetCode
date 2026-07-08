import numpy as np


def kl_divergence(p, q, eps=1e-12):
    # 1. KL(p||q) = sum p * log(p / q)，clip 防止 log(0)。
    p = np.clip(np.asarray(p, dtype=float), eps, 1.0)
    q = np.clip(np.asarray(q, dtype=float), eps, 1.0)
    return float(np.sum(p * np.log(p / q)))


def cross_entropy(p, q, eps=1e-12):
    # 1. 交叉熵 H(p, q) = -sum p * log(q)。
    p = np.asarray(p, dtype=float)
    q = np.clip(np.asarray(q, dtype=float), eps, 1.0)
    return float(-np.sum(p * np.log(q)))


if __name__ == "__main__":
    p = np.array([0.7, 0.3])
    q = np.array([0.6, 0.4])
    print(kl_divergence(p, q), cross_entropy(p, q))
