from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(current_index, memory):
            memory.append(candidates[current_index])

            if sum(memory) == target:
                ans.append(memory[:])
            elif sum(memory) > target:
                memory.pop()
                return

            for i in range(current_index, len(candidates)):
                dfs(i, memory)

            memory.pop()

        for i in range(len(candidates)):
            dfs(i, [])

        return ans