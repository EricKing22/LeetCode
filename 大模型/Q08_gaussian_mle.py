import numpy as np


def gaussian_mle(X, full_cov=True, eps=1e-12):
    # 1. 高斯分布极大似然估计：均值取样本均值。
    X = np.asarray(X, dtype=float)
    mean = X.mean(axis=0)
    Xc = X - mean
    if full_cov:
        # 2. full_cov=True 时估计完整协方差矩阵。
        cov = Xc.T @ Xc / len(X)
        cov = cov + np.eye(cov.shape[0]) * eps
        return mean, cov

    # 3. full_cov=False 时只估计每个维度独立的方差。
    var = (Xc ** 2).mean(axis=0) + eps
    return mean, var


if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4]], dtype=float)
    print(gaussian_mle(X))
