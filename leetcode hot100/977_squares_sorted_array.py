from typing import List
import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        ans = []
        while left < right:
            left_square = nums[left]**2
            right_square = nums[right] ** 2
            if left_square > right_square:
                ans = [left_square] + ans
                left += 1
            else:
                ans = [right_square] + ans
                right -= 1
        return ans