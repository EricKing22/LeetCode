import numpy as np
n, m, h = map(int, input().split())

def softmax(input_matrix):
    X = np.array(input_matrix)
    row_sum = X.sum(axis=1)
    for i in range(len(X)):
        X[i] /= row_sum[i]
    return X

X = np.ones((n,h))
W1 = np.zeros((m,h))
W2 = np.zeros((m,h))
W3 = np.zeros((m,h))

for i in range(m):
    for j in range(h):
        if j >= i:
            W1[i][j] = 1
            W2[i][j] = 1
            W3[i][j] = 1

# Compute
Q = np.matmul(X, W1.T)
K = np.matmul(X, W2.T)
V = np.matmul(X, W3.T)

result = np.matmul(softmax((Q@K.T)/np.sqrt(h)), V)

print(int(result.sum()))
