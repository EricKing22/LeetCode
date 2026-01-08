from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dp = [0 for _ in temperatures]

        for i in range(len(temperatures) - 2, -1, -1):

            if temperatures[i] >= temperatures[i + 1]:
                next_hot_index = i + 1
                find = True

                while temperatures[i] >= temperatures[next_hot_index]:
                    if dp[next_hot_index] == 0:
                        find = False
                        break
                    next_hot_index += dp[next_hot_index]

                if not find:
                    dp[i] = 0
                else:
                    dp[i] = next_hot_index - i
            elif temperatures[i] < temperatures[i + 1]:
                dp[i] = 1

        return dp