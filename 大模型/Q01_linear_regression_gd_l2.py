import numpy as np


def linear_regression_gd_l2(
    X, y, lr=0.05, epochs=1000, l2=0.0, fit_intercept=True
):
    """Use batch gradient descent to fit y = X @ w + b."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    y = np.asarray(y, dtype=float).reshape(-1, 1)

    n_samples, n_features = X.shape
    w = np.zeros((n_features, 1))
    b = 0.0
    losses = []

    for _ in range(epochs):
        pred = X @ w + (b if fit_intercept else 0.0)
        err = pred - y

        grad_w = X.T @ err / n_samples + l2 * w
        grad_b = float(err.mean()) if fit_intercept else 0.0
        w -= lr * grad_w
        b -= lr * grad_b

        loss = (err ** 2).mean() / 2 + l2 * (w ** 2).sum() / 2
        losses.append(float(loss))

    return w.ravel(), float(b), losses


if __name__ == "__main__":
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([[3.0], [5.0], [7.0], [9.0]])
    print(linear_regression_gd_l2(X, y, epochs=2000)[:2])
