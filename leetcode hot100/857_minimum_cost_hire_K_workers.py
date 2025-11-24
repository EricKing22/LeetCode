import math
from typing import List
class Solution:
    def __init__(self):
        self.pay_min = math.inf

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        num_workers = len(quality)
        def dfs(quality, wage, workers, expect_wages, ratio, cur_sum):
            if len(workers) == k:
                if cur_sum > self.pay_min:
                    return
                self.pay_min = min(self.pay_min, cur_sum)
                return

            for i in range(num_workers):
                if i in workers:
                    pass
                else:
                    pay_wage = quality[i] * ratio
                    if pay_wage >= wage[i]:
                        expect_wages.append(pay_wage)
                        workers.append(i)
                        dfs(quality, wage, workers, expect_wages, ratio, cur_sum + pay_wage)
                        workers.pop()
                        expect_wages.pop()



        for i in range(num_workers):
            ratio = wage[i] / quality[i]
            dfs(quality, wage, [i], [wage[i]], ratio, wage[i])

        return self.pay_min