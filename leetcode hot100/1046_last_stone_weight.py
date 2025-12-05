from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort(reverse=True)

        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        else:
            s1, s2 = stones[0], stones[1]
            stones = stones[2:]



        new_s = s1 - s2 if s1 - s2 >= 0 else s2 - s1

        if new_s != 0:
            stones = [new_s] + stones

        return self.lastStoneWeight(stones)
