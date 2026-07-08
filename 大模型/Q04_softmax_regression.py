import numpy as np


def add_bias(X):
    # 1. 多分类线性分类器也通过拼接常数 1 来学习 bias。
    X = np.asarray(X, dtype=float)
    return np.c_[np.ones((X.shape[0], 1)), X]


def stable_softmax_np(logits, axis=-1):
    # 1. 先减去最大值，不改变 softmax 结果，但能防止 exp 溢出。
    logits = np.asarray(logits, dtype=float)
    z = logits - logits.max(axis=axis, keepdims=True)
    exp_z = np.exp(z)
    return exp_z / exp_z.sum(axis=axis, keepdims=True)


def softmax_regression(X, y, num_classes=None, lr=0.1, epochs=1000, l2=0.0):
    # 1. X_train: [N, D+1]，W: [D+1, C]，Y 是 one-hot 标签。
    X_train = add_bias(X)
    y = np.asarray(y, dtype=int)
    num_classes = int(num_classes or (y.max() + 1))
    W = np.zeros((X_train.shape[1], num_classes))
    Y = np.eye(num_classes)[y]

    for _ in range(epochs):
        # 2. 前向：logits = XW，再用 softmax 得到类别概率。
        prob = stable_softmax_np(X_train @ W, axis=1)

        # 3. 正则项不惩罚 bias 行。
        reg = W.copy()
        reg[0] = 0.0

        # 4. softmax + cross entropy 的梯度是 X^T(prob - Y)。
        grad = X_train.T @ (prob - Y) / len(X_train) + l2 * reg
        W -= lr * grad

    # 5. 返回普通权重矩阵和每个类别的 bias。
    return W[1:], W[0]


if __name__ == "__main__":
    X = np.array([[0.0], [1.0], [2.0], [3.0]])
    y = np.array([0, 0, 1, 2])
    print(softmax_regression(X, y, num_classes=3)[:2])
