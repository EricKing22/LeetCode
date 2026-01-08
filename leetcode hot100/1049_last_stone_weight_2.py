from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        target = total // 2
        dp = [0] * (target + 1)
        for weight in stones:
            for i in range(target, weight-1, -1):
                dp[i] = min(dp[i], dp[i - weight] + weight)

        return dp[target]
