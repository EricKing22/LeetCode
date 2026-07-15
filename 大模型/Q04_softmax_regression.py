import numpy as np


def stable_softmax_np(logits, axis=-1):
    logits = np.asarray(logits, dtype=float)
    shifted = logits - logits.max(axis=axis, keepdims=True)
    exp_shifted = np.exp(shifted)
    return exp_shifted / exp_shifted.sum(axis=axis, keepdims=True)


def softmax_regression(
    X, y, num_classes=None, lr=0.1, epochs=1000, l2=0.0, fit_intercept=True
):
    """Use batch gradient descent to fit softmax(X @ W + b)."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    y = np.asarray(y, dtype=int).reshape(-1)

    n_samples, n_features = X.shape
    num_classes = int(num_classes or (y.max() + 1))
    W = np.zeros((n_features, num_classes))
    b = np.zeros((1, num_classes))
    Y = np.eye(num_classes)[y]

    for _ in range(epochs):
        logits = X @ W + (b if fit_intercept else 0.0)
        prob = stable_softmax_np(logits, axis=1)
        err = prob - Y

        grad_W = X.T @ err / n_samples + l2 * W
        grad_b = err.mean(axis=0, keepdims=True) if fit_intercept else 0.0
        W -= lr * grad_W
        b -= lr * grad_b

    return W, b.ravel()


if __name__ == "__main__":
    X = np.array([[0.0], [1.0], [2.0], [3.0]])
    y = np.array([0, 0, 1, 2])
    print(softmax_regression(X, y, num_classes=3)[:2])
