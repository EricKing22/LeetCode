import numpy as np


def cosine_topk(query, matrix, k=5, eps=1e-12):
    # 1. 先把 query 和候选向量都归一化，点积就等于余弦相似度。
    query = np.asarray(query, dtype=float)
    matrix = np.asarray(matrix, dtype=float)
    q = query / (np.linalg.norm(query) + eps)
    M = matrix / (np.linalg.norm(matrix, axis=1, keepdims=True) + eps)
    scores = M @ q

    # 2. 先取 top-k 的无序下标，再按分数降序排好。
    idx = np.argpartition(-scores, kth=k - 1)[:k]
    idx = idx[np.argsort(-scores[idx])]
    return idx, scores[idx]


if __name__ == "__main__":
    matrix = np.eye(4)
    print(cosine_topk(np.array([1, 0.2, 0, 0]), matrix, k=2))
