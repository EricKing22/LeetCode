from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        capacity = (total + target) // 2

        dp = [0] * (len(nums) + 1)
        for num in nums:
            for i in range(capacity, num-1, -1):
                dp[i] += dp[i-num]

        return dp[capacity]