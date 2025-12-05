from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(current_index, memory):
            if nums[current_index] not in memory:
                memory.append(nums[current_index])
            print(memory)
            if len(memory) == len(nums):
                ans.append(memory[:])

            unvisited = []
            for i in range(len(nums)):
                if nums[i] not in memory:
                    unvisited.append(i)

            for i in unvisited:
                dfs(i, memory)

            memory.pop()

        for i in range(len(nums)):
            dfs(i, [])

        ans.sort()
        return ans
