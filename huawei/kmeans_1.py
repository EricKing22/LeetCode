import math
from collections import defaultdict
import numpy as np
k,m,n = list(map(int, input().split()))

features = []
for _ in range(m):
    features.append(list(map(float, input().split())))

def cal_distance(x1, x2):
    x1 = np.array(x1)
    x2 = np.array(x2)

    return np.sqrt(np.sum(np.square(x1-x2)))

centers = features[:k]


for _ in range(n):
    centers_group = defaultdict(list)
    for feature in features:
        min_distance = math.inf
        for idx, center in enumerate(centers):
            distance = cal_distance(feature, center)
            if distance < min_distance:
                assigned_center = idx
                min_distance = min(min_distance, distance)

        centers_group[assigned_center].append(feature)

    new_centers = []
    for (_,item) in centers_group.items(): # center,features
        fs = np.array(item)
        fs = fs.mean(axis=0)
        new_centers.append(fs)

    stop = []
    for center, new_center in zip(centers, new_centers):
        if cal_distance(center, new_center) < 1e-8:
            stop.append(True)
        else:
            stop.append(False)
    if np.all(np.array(stop)):
        centers = new_centers
        break

    centers = new_centers



centers_group = defaultdict(list)
for feature in features:
    min_distance = math.inf
    for idx, center in enumerate(centers):
        distance = cal_distance(feature, center)
        if distance < min_distance:
            assigned_center = idx
            min_distance = min(min_distance, distance)

    centers_group[assigned_center].append(feature)

ans = []
for (_,item) in centers_group.items():
    ans.append(len(item))

ans.sort()

print(" ".join([str(item) for item in ans]))