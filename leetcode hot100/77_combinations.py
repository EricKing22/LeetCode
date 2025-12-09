from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def dfs(current, memory):
            memory.append(current)

            if len(memory) == k:
                ans.append(memory[:])
                memory.pop()
                return

            for i in range(current + 1, n):
                dfs(i, memory)

            memory.pop()

        for i in range(1,n):
            dfs(i,[])

        return ans
