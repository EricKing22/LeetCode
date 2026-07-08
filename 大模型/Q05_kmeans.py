import numpy as np


def kmeans(X, k, max_iter=100, tol=1e-4, seed=0):
    # 1. 随机选择 k 个样本作为初始中心。
    X = np.asarray(X, dtype=float)
    rng = np.random.default_rng(seed)
    centers = X[rng.choice(len(X), size=k, replace=False)].copy()

    for _ in range(max_iter):
        # 2. 计算每个样本到每个中心的平方距离，并分配到最近簇。
        dist2 = ((X[:, None, :] - centers[None, :, :]) ** 2).sum(axis=2)
        labels = dist2.argmin(axis=1)
        new_centers = centers.copy()

        for j in range(k):
            points = X[labels == j]
            if len(points) == 0:
                # 3. 空簇用“当前最难解释”的点重新初始化，避免中心失效。
                farthest = dist2.min(axis=1).argmax()
                new_centers[j] = X[farthest]
            else:
                # 4. 非空簇的中心更新为簇内样本均值。
                new_centers[j] = points.mean(axis=0)

        # 5. 如果中心移动很小，认为已经收敛。
        shift = np.linalg.norm(new_centers - centers)
        centers = new_centers
        if shift < tol:
            break
    return centers, labels


if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [8, 8], [8, 9], [50, 50]], dtype=float)
    print(kmeans(X, k=3, seed=0))
