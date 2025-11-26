L, D = map(int,input().split(","))
import numpy as np

elements = list(map(float, input().split(",")))
elements = np.array(elements).reshape((L,D))


Wq1 = list(map(float, input().split(",")))
Wq1 = np.array(Wq1).reshape((D,D))
Wk1 = list(map(float, input().split(",")))
Wk1 = np.array(Wk1).reshape((D,D))
Wv1 = list(map(float, input().split(",")))
Wv1 = np.array(Wv1).reshape((D,D))

Wfc1 = list(map(float, input().split(",")))
Wfc1 = np.array(Wfc1).reshape((D,D))
Bfc1 = list(map(float, input().split(",")))
Bfc1 = np.array(Bfc1)

Wq2 = list(map(float, input().split(",")))
Wq2 = np.array(Wq2).reshape((D,D))
Wk2 = list(map(float, input().split(",")))
Wk2 = np.array(Wk2).reshape((D,D))
Wv2 = list(map(float, input().split(",")))
Wv2 = np.array(Wv2).reshape((D,D))

Wfc2 = list(map(float, input().split(",")))
Wfc2 = np.array(Wfc2).reshape((D,D))
Bfc2 = list(map(float, input().split(",")))
Bfc2 = np.array(Bfc2)

def self_attention(Wq, Wk, Wv, x, d):
    Q = x @ np.array(Wq).T
    K = x @ np.array(Wk).T
    V = x @ np.array(Wv).T

    QKT = (Q @ K.T) / np.sqrt(d)
    result = softmax(QKT) @ V

    return result

def softmax(X):
    for i in range(len(X)):
        row = X[i]
        exp = np.exp(row)
        exp_sum = sum(exp)
        X[i] = exp / exp_sum
    return X

sa1_result = self_attention(Wq1, Wk1, Wv1, elements, D)
fc1_result = sa1_result @ Wfc1.T + Bfc1
sa2_result = self_attention(Wq2, Wk2, Wv2, fc1_result, D)
fc2_result = sa2_result @ Wfc2.T + Bfc2


result = fc2_result.ravel()
ans = ",".join(f"{r:.2f}" for r in result)
print(ans)