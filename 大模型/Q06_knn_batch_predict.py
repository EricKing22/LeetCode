import numpy as np


def knn_predict_batch(X_train, y_train, X_test, k=5):
    # 1. 统一数据类型，方便后面用广播一次性算所有测试样本的距离。
    X_train = np.asarray(X_train, dtype=float)
    X_test = np.asarray(X_test, dtype=float)
    y_train = np.asarray(y_train, dtype=int)

    # 2. dist2 的形状是 [测试样本数, 训练样本数]。
    dist2 = ((X_test[:, None, :] - X_train[None, :, :]) ** 2).sum(axis=2)

    # 3. argpartition 只找前 k 个近邻，比完整排序更省。
    nn_idx = np.argpartition(dist2, kth=k - 1, axis=1)[:, :k]
    votes = y_train[nn_idx]

    # 4. 对每个测试样本做多数投票，票数相同时返回较小的类别编号。
    return np.array([np.bincount(row).argmax() for row in votes])


if __name__ == "__main__":
    X_train = np.array([[0, 0], [0, 1], [5, 5], [6, 5]], dtype=float)
    y_train = np.array([0, 0, 1, 1])
    X_test = np.array([[0.2, 0.1], [5.2, 5.1]], dtype=float)
    print(knn_predict_batch(X_train, y_train, X_test, k=3))
