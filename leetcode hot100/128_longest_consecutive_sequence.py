from typing import List


class Solution:
    def __init__(self):
        self.ans = 1

    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        memory = [0]

        if nums == []:
            return 0

        def dfs(current_index, memory):
            if current_index == len(nums) - 1:
                return

            if nums[current_index + 1] == nums[memory[-1]] + 1:
                memory.append(current_index + 1)
                self.ans = max(self.ans, len(memory))
                dfs(current_index + 1, memory)
                memory.pop()
            elif nums[current_index + 1] == nums[memory[-1]]:
                dfs(current_index + 1, memory)
            else:
                dfs(current_index + 1, [current_index + 1])

        dfs(0, memory)

        return self.ans


