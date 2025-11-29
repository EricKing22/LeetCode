from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(current_index, memory):
            memory.append(current_index)

            if len(memory) == len(nums):
                ans.append(memory[:])

            for i in range(len(nums)):
                if i not in memory:
                    dfs(i, memory)

            memory.pop()

        result = []
        for i in range(len(nums)):
            dfs(i, [])
        for a in ans:
            items = [nums[index] for index in a]
            if items not in result:
                result.append(items)

        return result