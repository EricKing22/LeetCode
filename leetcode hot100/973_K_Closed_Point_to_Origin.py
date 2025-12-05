import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def cal_distance(l1,l2):
            sq_sum = 0
            for x1,x2 in zip(l1,l2):
                sq_sum += (x1-x2) ** 2
            return math.sqrt(sq_sum)

        distances = []
        for point in points:
            distances.append((point,cal_distance(point, [0,0])))

        distances.sort(key=lambda x : x[-1])
        distances = distances[:k]
        ans = []
        for point, _ in distances:
            ans.append(point)
        return ans