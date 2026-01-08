from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:


        total = sum(nums)
        if total % 2 != 0:
            return False

        target = sum(nums) // 2
        dp = [0] * (target+1)
        for n in nums:
            # decreasing from capacity to num
            for i in range(target, n-1, -1):
                dp[i] = max(dp[i], dp[i-n]+n)

                if dp[i] == target:
                    return True

        return False
