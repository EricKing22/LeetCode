import numpy as np

from Q05_kmeans import kmeans


# Q5: K-Means with empty-cluster reset.
if __name__ == "__main__":
    X = np.array([[0, 0], [0, 1], [8, 8], [8, 9], [50, 50]], dtype=float)
    centers, labels = kmeans(X, k=3, seed=0)
    print("centers:\n", centers)
    print("labels:", labels)
