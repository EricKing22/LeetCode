from collections import defaultdict

import numpy as np

N = 50
K = 5
epoch = 10
tol = 5
features = [list(map(float,input().split())) for _ in range(N)]

centers = features[:K]

def cal_distance(l1,l2):
    l1 = np.array(l1)
    l2 = np.array(l2)

    return np.sqrt(np.sum((l1-l2) ** 2))



for _ in range(epoch):
    groups = defaultdict(list)
    for feature in features:
        distances = []
        for center in centers:
            distance = cal_distance(feature, center)
            distances.append(distance)
        target_idx = np.argmin(distances)
        groups[target_idx].append(feature)

    for i in range(K):
        centers[i] = np.array(groups[i]).mean(axis=0).tolist()


print(centers)


