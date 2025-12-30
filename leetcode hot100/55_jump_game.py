from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return True


        dp = [0 for _ in nums]

        dp[-1] = 1

        end_i = len(nums) - 1
        i = len(dp) - 2

        while i >=  0:
            if nums[i] + i >= end_i:
                dp[i] = 1
                end_i = i

            i -= 1

        return dp[0] == 1
