from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        memory = [nums[0]]

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                memory.append(nums[i])
            else:
                if len(memory) == 1:
                    ans.append(str(memory[0]))
                else:
                    ans.append(str(memory[0]) + "->" + str(memory[-1]))
                memory = [nums[i]]

        if len(memory) == 1:
            ans.append(str(memory[0]))
        else:
            ans.append(str(memory[0]) + "->" + str(memory[-1]))


        return ans