import math
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 1
        right = len(nums)
        nums = [-math.inf] + nums + [math.inf]

        def condition(mid):
            if nums[mid] < nums[mid + 1]:
                return True
            else:
                return False

        while left < right:

            mid = left + (right - left) // 2

            if condition(mid):
                left = mid + 1
            else:
                right = mid


        return left