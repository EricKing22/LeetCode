import numpy as np
b, d, r = list(map(int, input().split()))

x = list(map(float, input().split()))
Wq = list(map(float, input().split()))
Wk = list(map(float, input().split()))
Wv = list(map(float, input().split()))

A, B = None, None
if r > 0:
    A = list(map(float, input().split()))
    B = list(map(float, input().split()))
    A = np.array(A).reshape((r, d))
    B = np.array(B).reshape((d, r))

x = np.array(x).reshape((b, d))
Wq = np.array(Wq).reshape((d,d))
Wk = np.array(Wk).reshape((d,d))
Wv = np.array(Wv).reshape((d,d))



def LoRA_Attention(x, Wq, Wk, Wv, A, B):
    if A is not None:
        Wq = Wq + (B @ A)

    Q = x @ Wq.T
    K = x @ Wk.T
    V = x @ Wv.T

    def softmax(x):
        x = np.array(x)
        max_vals = np.max(x, axis=1, keepdims=True)
        x -= max_vals
        exp_sum = np.sum(np.exp(x), axis=1, keepdims=True)
        return (np.exp(x))/ exp_sum

    result = softmax((Q @ K.T )/ np.sqrt(d)) @ V
    result = result.ravel()
    ans = []
    for i in range(len(result)):
        ans.append(f"{result[i]:.4f}")


    print(" ".join(ans))

LoRA_Attention(x, Wq, Wk, Wv, A, B)