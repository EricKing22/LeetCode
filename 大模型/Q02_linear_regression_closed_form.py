import numpy as np


def add_bias(X):
    # 1. 闭式解同样用第一列全 1 表示截距项。
    X = np.asarray(X, dtype=float)
    return np.c_[np.ones((X.shape[0], 1)), X]


def linear_regression_closed_form(X, y, l2=0.0, fit_intercept=True):
    # 1. 整理输入形状，确保矩阵乘法维度稳定。
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    X_train = add_bias(X) if fit_intercept else X

    # 2. Ridge 正则矩阵：默认不惩罚 bias/intercept。
    reg = np.eye(X_train.shape[1]) * l2
    if fit_intercept:
        reg[0, 0] = 0.0

    # 3. 闭式解：w = (X^T X + lambda I)^+ X^T y，用 pinv 提升数值稳定性。
    w = np.linalg.pinv(X_train.T @ X_train + reg) @ X_train.T @ y

    # 4. 拆分返回普通权重和截距。
    if fit_intercept:
        return w[1:].ravel(), float(w[0])
    return w.ravel(), 0.0


if __name__ == "__main__":
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([3.0, 5.0, 7.0, 9.0])
    print(linear_regression_closed_form(X, y))
