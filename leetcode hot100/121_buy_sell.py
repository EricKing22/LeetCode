import math


def maxProfit(prices):
    profit_max = 0
    buy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        profit_max = max(profit_max, prices[i]-buy)
    return profit_max