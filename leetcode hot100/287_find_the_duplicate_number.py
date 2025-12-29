from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        prev = 0
        x = nums[0]
        nums[0] = -1
        while x != -1:
            prev = x
            x = nums[x]
            nums[prev] = -1

        return prev

