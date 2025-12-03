import math
import sys

import numpy as np
from collections import defaultdict
data = []
while True:
    try:
        line = input()
        data.append(list(map(float, line.split())))
    except EOFError:
        break

class Node:
    def __init__(self, idx, arr):
        self.idx = idx
        self.arr = arr

nodes = []

if len(data) == 0:
    print(0)
    sys.exit()

arr_length = len(data[0]) - 1
max_idx = 0

for d in data:
    idx, arr = d[0], d[1:]
    max_idx = int(idx)

    if len(arr) != arr_length:
        print(0)
        sys.exit()

    node = Node(idx, arr)
    nodes.append(node)


def cos_sim(l1, l2):
    dot_prod = 0
    for x,y in zip(l1,l2):
        dot_prod += x*y

    l1_norm = np.mean(np.array(l1) ** 2)
    l2_norm = np.mean(np.array(l2) ** 2)
    if l1_norm == 0 or l2_norm ==0:
        return 0

    return dot_prod / (l1_norm * l2_norm)
def is_close(l1,l2):
    sim = cos_sim(l1,l2)
    return sim >= 0.95

def union(node1, node2):
    if node1.idx < node2.idx:
        node2.idx = node1.idx
    else:
        node1.idx = node2.idx


for i in range(0, max_idx):
    node1 = nodes[i]
    for j in range(i+1, max_idx):
        node2 = nodes[j]
        if is_close(node1.arr, node2.arr):
            union(node1, node2)

clusters = defaultdict(list)

for node in nodes:
    idx = node.idx
    clusters[idx].append(node)

# unable to cluster
if len(clusters.keys()) == len(data):
    print(1)
else:
    max_length = 0
    for _,values in clusters.items():
        max_length = max(max_length, len(values))
    print(str(max_length))