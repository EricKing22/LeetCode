import numpy as np


def add_bias(X):
    # 1. 在特征前拼一列 1，用线性层的第 0 个权重表示 bias。
    X = np.asarray(X, dtype=float)
    return np.c_[np.ones((X.shape[0], 1)), X]


def sigmoid(x):
    # 1. 分正负区间计算 sigmoid，避免 exp 在大负数/大正数时溢出。
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    pos = x >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    exp_x = np.exp(x[~pos])
    out[~pos] = exp_x / (1.0 + exp_x)
    return out


def logistic_regression_binary(X, y, lr=0.1, epochs=1000, l2=0.0):
    # 1. 二分类逻辑回归：prob = sigmoid(Xw)。
    X_train = add_bias(X)
    y = np.asarray(y, dtype=float).reshape(-1, 1)
    w = np.zeros((X_train.shape[1], 1))

    for _ in range(epochs):
        # 2. 交叉熵对 logits 的梯度是 prob - y。
        prob = sigmoid(X_train @ w)

        # 3. L2 正则不作用在 bias 上。
        reg = w.copy()
        reg[0] = 0.0

        # 4. 批量梯度下降更新参数。
        grad = X_train.T @ (prob - y) / len(X_train) + l2 * reg
        w -= lr * grad

    # 5. 返回权重和截距。
    return w[1:].ravel(), float(w[0])


if __name__ == "__main__":
    X = np.array([[0.0], [1.0], [2.0], [3.0]])
    y = np.array([0, 0, 1, 1])
    print(logistic_regression_binary(X, y))
