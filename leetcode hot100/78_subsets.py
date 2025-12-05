from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def dfs(current_index, memory):
            memory.append(nums[current_index])
            ans.append(memory[:])

            for i in range(current_index+1, len(nums)):
                dfs(i, memory)

            memory.pop()

        for i in range(len(nums)):
            dfs(i,[])

        return ans
