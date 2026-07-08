import numpy as np

from Q06_knn_batch_predict import knn_predict_batch


# Q6: KNN batch prediction.
if __name__ == "__main__":
    X_train = np.array([[0, 0], [0, 1], [5, 5], [6, 5]], dtype=float)
    y_train = np.array([0, 0, 1, 1])
    X_test = np.array([[0.2, 0.1], [5.2, 5.1]], dtype=float)
    print(knn_predict_batch(X_train, y_train, X_test, k=3))
