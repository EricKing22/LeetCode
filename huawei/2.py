import numpy as np

n,d,c = list(map(int,input().split()))

X = []
for _ in range(n):
    X.append(list(map(float,input().split())))

W = []
for _ in range(d):
    W.append(list(map(float,input().split())))

ratio = float(input())

W = np.array(W)

W_row_sum = W.sum(axis=1).tolist()


row_sums = []
for i,row_sum in enumerate(W_row_sum):
    row_sums.append((i,row_sum))
row_sums.sort(key=lambda x : x[1])

k = max(int(ratio * d), 1)

remove_row_idx = [i for i,row_sum in row_sums[:k]]

X_T = np.array(X).T.tolist()
X_new = []
W_new = []
for i,row in enumerate(W):
    if i not in remove_row_idx:
        W_new.append(row)
        X_new.append(X_T[i])
X_new = np.array(X_new).T

# predict

W_new = np.array(W_new)


def softmax(h):
    h = np.array(h)
    h = h - h.max()

    exp_sum = np.sum(np.exp(h))

    return np.exp(h) / exp_sum

H = X_new @ W_new
preds = []
for row in H:
    preds.append(softmax(row))



ans = np.array(preds).argmax(axis=1).tolist()
print(" ".join([str(item) for item in ans]))

