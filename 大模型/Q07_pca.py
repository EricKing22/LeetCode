import numpy as np


def pca(X, n_components):
    # 1. PCA 先对每个特征去均值，让主成分描述方差方向。
    X = np.asarray(X, dtype=float)
    mean = X.mean(axis=0, keepdims=True)
    Xc = X - mean

    # 2. 构造协方差矩阵，并做特征值分解。
    cov = Xc.T @ Xc / (len(Xc) - 1)
    eigvals, eigvecs = np.linalg.eigh(cov)

    # 3. 特征值越大说明该方向解释的方差越多，按降序取前 n_components 个。
    order = eigvals.argsort()[::-1]
    components = eigvecs[:, order[:n_components]]
    explained = eigvals[order[:n_components]]

    # 4. 返回降维后的数据、主成分方向、解释方差和均值。
    return Xc @ components, components, explained, mean.ravel()


if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [8, 9]], dtype=float)
    print(pca(X, 1)[0])
