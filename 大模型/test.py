import numpy as np


def linear_regression_gd_l2(X,y,lr=0.05,epochs=1000):
    X = np.array(X)
    y = np.array(y).reshape(-1,1)

    w = np.zeros((X.shape[-1], 1))
    b = 0.0

    for _ in range(epochs):
        pred = X @ w + b

        error = pred - y

        grad_w = X.T @ error
        grad_b = error.mean()

        w -= lr * grad_w
        b -= lr * grad_b

    return w,b

def distance(a,b):
    a = np.array(a)
    b = np.array(b)

    return np.sqrt( ((a - b) ** 2).sum())

if __name__ == "__main__":
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([[3.0], [5.0], [7.0], [9.0]])
    print(linear_regression_gd_l2(X, y, epochs=2000)[:2])