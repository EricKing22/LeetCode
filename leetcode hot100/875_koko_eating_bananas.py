import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def condition(speed):
            if speed == 0:
                return True
            cost = 0
            for pile in piles:
                cost += math.ceil(pile / speed)
            return cost > h

        left, right = 0, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                left = mid + 1
            else:
                right = mid

        return left
