import numpy as np


def linear_regression_closed_form(X, y, l2=0.0, fit_intercept=True):
    """Solve y = X @ w + b with the regularized normal equation."""
    X = np.asarray(X, dtype=float)
    if X.ndim == 1:
        X = X.reshape(-1, 1)
    y = np.asarray(y, dtype=float).reshape(-1, 1)

    n_features = X.shape[1]
    reg = np.eye(n_features) * l2

    if fit_intercept:
        x_mean = X.mean(axis=0, keepdims=True)
        y_mean = y.mean(axis=0, keepdims=True)
        X_centered = X - x_mean
        y_centered = y - y_mean
        w = np.linalg.pinv(X_centered.T @ X_centered + reg)
        w = w @ X_centered.T @ y_centered
        b = y_mean - x_mean @ w
    else:
        w = np.linalg.pinv(X.T @ X + reg) @ X.T @ y
        b = np.zeros((1, 1))

    return w.ravel(), float(b.squeeze())


if __name__ == "__main__":
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([[3.0], [5.0], [7.0], [9.0]])
    print(linear_regression_closed_form(X, y))
