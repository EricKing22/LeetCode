from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def dfs(current_index, memory):
            memory.append(nums[current_index])

            if len(memory) == len(nums):
                ans.append(memory[:])

            for i in range(len(nums)):
                if nums[i] in memory:
                    pass
                else:
                    dfs(i, memory)
            memory.pop()

        for i in range(len(nums)):
            dfs(i, [])
        return ans
