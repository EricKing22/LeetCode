import numpy as np


class MLP:
    def __init__(self, input_size, hidden_size, output_size, lr=0.1):
        # 1. 随机初始化权重 (使用简单的正态分布)
        self.W1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))
        self.lr = lr

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_derivative(self, x):
        # Sigmoid 的导数：f(x) * (1 - f(x))
        return x * (1 - x)

    def forward(self, X):
        # 前向传播
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self._sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self._sigmoid(self.z2)
        return self.a2

    def backward(self, X, y, output):
        # 反向传播 (核心环节)

        # 1. 计算输出层的误差梯度
        # dL/da2 * da2/dz2
        error_output = output - y
        delta_output = error_output * self._sigmoid_derivative(output)

        # 2. 计算隐藏层的误差梯度
        # delta_output * W2.T * da1/dz1
        error_hidden = np.dot(delta_output, self.W2.T)
        delta_hidden = error_hidden * self._sigmoid_derivative(self.a1)

        # 3. 更新权重和偏置 (梯度下降)
        # W = W - lr * (input.T * delta)
        self.W2 -= self.lr * np.dot(self.a1.T, delta_output)
        self.b2 -= self.lr * np.sum(delta_output, axis=0, keepdims=True)
        self.W1 -= self.lr * np.dot(X.T, delta_hidden)
        self.b1 -= self.lr * np.sum(delta_hidden, axis=0, keepdims=True)

    def train(self, X, y, epochs=10000):
        for i in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            if i % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {i}, Loss: {loss:.4f}")


# --- 测试一下：解决 XOR 问题 ---
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

mlp = MLP(input_size=2, hidden_size=4, output_size=1, lr=0.5)
mlp.train(X, y)

# 最终预测
print("\nFinal Predictions:")
print(mlp.forward(X))