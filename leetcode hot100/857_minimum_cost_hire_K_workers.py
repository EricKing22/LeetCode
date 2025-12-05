import math
from typing import List
class Solution:
    def __init__(self):
        self.pay_min = math.inf

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        num_workers = len(quality)


        def dfs(current_index, memory):
            if memory != []:
                index = memory[0]
                ratio = wage[index] / quality[index]
            else:
                ratio = wage[current_index] / quality[current_index]

            memory.append(current_index)

            if len(memory) == k:
                pay_sum = 0
                valid = True
                for index in memory:
                    if wage[index] > quality[index] * ratio:
                        valid = False
                        break
                    else:
                        pay_sum += quality[index] * ratio

                if valid:
                    self.pay_min = min(self.pay_min, pay_sum)

            for i in range(num_workers):
                if i not in memory:
                    dfs(i, memory)

            memory.pop()

        for i in range(num_workers):
            dfs(i, [])

        return self.pay_min


