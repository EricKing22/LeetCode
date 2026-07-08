import numpy as np


def add_bias(X):
    # 1. 把输入转成浮点数组，并在最前面拼一列 1 表示 bias/intercept。
    X = np.asarray(X, dtype=float)
    return np.c_[np.ones((X.shape[0], 1)), X]


def linear_regression_gd_l2(X, y, lr=0.05, epochs=1000, l2=0.0, fit_intercept=True):
    # 1. 统一输入形状：X 是 [样本数, 特征数]，y 是 [样本数, 1]。
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    X_train = add_bias(X) if fit_intercept else X

    # 2. 权重从 0 开始迭代，losses 用来记录每轮的目标函数值。
    w = np.zeros((X_train.shape[1], 1))
    losses = []

    for _ in range(epochs):
        # 3. 前向计算预测值和误差：pred = Xw，err = pred - y。
        pred = X_train @ w
        err = pred - y

        # 4. L2 正则不惩罚 bias，所以拟合截距时把 reg[0] 置 0。
        reg = w.copy()
        if fit_intercept:
            reg[0] = 0.0

        # 5. 梯度 = 均方误差梯度 + L2 正则梯度，然后做梯度下降更新。
        grad = X_train.T @ err / len(X_train) + l2 * reg
        w -= lr * grad

        # 6. 记录 1/2 MSE + 1/2 L2，方便观察训练是否收敛。
        losses.append(float((err ** 2).mean() / 2 + l2 * (reg ** 2).sum() / 2))

    # 7. 返回时把 bias 和普通权重拆开，和常见接口保持一致。
    if fit_intercept:
        return w[1:].ravel(), float(w[0]), losses
    return w.ravel(), 0.0, losses


if __name__ == "__main__":
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([3.0, 5.0, 7.0, 9.0])
    print(linear_regression_gd_l2(X, y, epochs=2000)[:2])
