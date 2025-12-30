from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(1, len(prices)-1):
            dif = prices[i] - prices[i-1]
            if dif > 0:
                profit += dif

        return profit


