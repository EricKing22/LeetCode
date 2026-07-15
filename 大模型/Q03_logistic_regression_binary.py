import numpy as np


def sigmoid(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    positive = x >= 0
    out[positive] = 1.0 / (1.0 + np.exp(-x[positive]))
    exp_x = np.exp(x[~positive])
    out[~positive] = exp_x / (1.0 + exp_x)
    return out


def logistic_regression_binary(
    X, y, lr=0.1, epochs=1000, l2=0.0, fit_intercept=True
):
    """Use batch gradient descent to fit sigmoid(X @ w + b)."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    y = np.asarray(y, dtype=float).reshape(-1, 1)

    n_samples, n_features = X.shape
    w = np.zeros((n_features, 1))
    b = 0.0

    for _ in range(epochs):
        logits = X @ w + (b if fit_intercept else 0.0)
        prob = sigmoid(logits)
        err = prob - y

        grad_w = X.T @ err / n_samples + l2 * w
        grad_b = float(err.mean()) if fit_intercept else 0.0
        w -= lr * grad_w
        b -= lr * grad_b

    return w.ravel(), float(b)


if __name__ == "__main__":
    X = np.array([[0.0], [1.0], [2.0], [3.0]])
    y = np.array([[0.0], [0.0], [1.0], [1.0]])
    print(logistic_regression_binary(X, y))
