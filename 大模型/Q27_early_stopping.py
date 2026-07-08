class EarlyStopping:
    def __init__(self, patience=3, min_delta=0.0):
        # 1. patience 表示允许连续多少次没有明显提升。
        self.patience = patience
        self.min_delta = min_delta
        self.best = None
        self.bad_count = 0

    def step(self, metric):
        # 2. 这里默认 metric 越小越好，例如验证集 loss。
        if self.best is None or metric < self.best - self.min_delta:
            self.best = metric
            self.bad_count = 0
            return False

        # 3. 没有达到 min_delta 的提升就累计 bad_count。
        self.bad_count += 1
        return self.bad_count >= self.patience


if __name__ == "__main__":
    stopper = EarlyStopping(patience=2)
    print([stopper.step(x) for x in [3.0, 2.0, 2.1, 2.2]])
