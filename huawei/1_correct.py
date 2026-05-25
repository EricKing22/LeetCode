from collections import defaultdict
import numpy as np
N, M, K = list(map(int,input().split()))

features = []
for _ in range(N):
    features.append(list(map(int,input().split())))

new_features = list(map(int,input().split()))


def distance(l1,l2):
    l1 = np.array(l1)
    l2 = np.array(l2)
    return float(np.sqrt(np.sum((l1-l2) ** 2)))

clusters_centers = features[:K]

# balanced partitioning
if N % K != 0:
    r = N % K
    max_lens = list([N // K] * K)
    for i in range(r):
        max_lens[i] += 1
else:
    max_lens = list([N // K] * K)

finished = False
while not finished:
    clusters_group = defaultdict(list)
    for node in features:
        distances = []
        for idx, center in enumerate(clusters_centers):
            distances.append((idx,distance(node, center)))

        distances.sort(key=lambda x : x[1])

        for (idx, _) in distances:
            # try to insert at idx
            if len(clusters_group[idx]) < max_lens[idx]:
                clusters_group[idx].append(node)
                break

    new_centers = []
    for (_,group_features) in clusters_group.items():
        fs = np.array(group_features)
        fs = fs.mean(axis=0)
        fs = list(map(int,fs))

        new_centers.append(fs)

    if np.all(np.isclose(new_centers, clusters_centers)):
        finished = True
    else:
        clusters_centers = new_centers

idx_clusters_centers = [ (idx, center) for idx, center in enumerate(clusters_centers) ]
idx_clusters_centers.sort(key=lambda x : x[1])
for (_,center) in clusters_centers:
    print(" ".join([str(item) for item in center]))

distances = []
for idx, center in idx_clusters_centers:
    distances.append((idx, distance(new_features, center)))

distances.sort(key=lambda x: x[1])
for (idx, _) in distances:
    if len(clusters_group[idx]) <= max_lens[idx]:
        print(idx+1)
        break








clusters_centers.sort()
for center in clusters_centers:
    print(" ".join([str(item) for item in center]))

distances = []
for idx, center in enumerate(clusters_centers):
    distances.append((idx, distance(new_features, center)))

distances.sort(key=lambda x: x[1])
for (idx, _) in distances:
    if len(clusters_group[idx]) <= max_lens[idx]:
        print(idx+1)
        break









