from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:


        dp = []
        current_max = 1
        current_min = 1
        for num in nums:
            temp = current_max * num
            current_max = max(temp, current_min * num, num)
            current_min = min(temp, current_min * num, num)
            dp.append(current_max)

        return max(dp)