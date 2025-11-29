import math
from typing import List


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = left + k
        min_avg = sum(nums[left:right]) / k

        while right <= len(nums):
            window = nums[left:right]
            avg = sum(window) / k
            min_avg = max(min_avg, avg)

            left += 1
            right += 1

        return min_avg