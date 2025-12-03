import numpy as np
L, D, K, lr = list(map(float, input().split(",")))
L, D, K = int(L), int(D), int(K)
Y =  list(map(float,input().split(",")))
X = list(map(float,input().split(",")))


W_mlp = list(map(float,input().split(",")))
W_cls = list(map(float,input().split(",")))

X = np.array(X).reshape((L,D))
Y = np.array(Y)
W_mlp = np.array(W_mlp).reshape((D,D))
W_cls = np.array(W_cls).reshape((D,K))
# forward
Z = X @ W_mlp
Y_hat = Z @ W_cls
Y_pred = Y_hat.mean(axis=0)
# loss

E = Y_pred - Y
loss = np.mean(E ** 2)

# back
dy_hat = 2 / K * E
dY_seq = np.ones((L, K)) * (dy_hat / L)
dw_cls = Z.T @ dY_seq

dz = dY_seq @ W_cls.T
dw_mlp = X.T @ dz

# update
W_mlp -= lr * dw_mlp
W_cls -= lr * dw_cls


Y_pred = Y_pred.tolist()
print(",".join([str(f"{p:.2f}") for p in Y_pred]))

print(str(f"{loss:.2f}"))

W_mlp = W_mlp.ravel().tolist()
print(",".join([str(f"{item:.2f}") for item in W_mlp]))

W_cls = W_cls.ravel().tolist()
print(",".join([str(f"{item:.2f}") for item in W_cls]))

