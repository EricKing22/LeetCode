from collections import defaultdict

import numpy as np

N = 50
K = 5
features = [list(map(int,input().split())) for _ in range(N)]
classes = [int(input()) for _ in range(N)]
X = list(map(int,input().split()))

def distance(l1,l2):
    l1 = np.array(l1)
    l2 = np.array(l2)

    return np.sqrt(np.mean((l1-l2) ** 2))

distances = []
for (idx,feature) in enumerate(features):
    distances.append((idx, distance(feature, X)))

distances.sort(key=lambda x : x[-1])

possible_classes = [classes[idx] for idx,_ in distances[:K]]

count = defaultdict(int)
for possible_class in possible_classes:
    count[possible_class] += 1

max_frequency = 0
ans = None
for idx,frequency in count.items():
    if frequency > max_frequency:
        ans = idx
        max_frequency = frequency

print(ans)


