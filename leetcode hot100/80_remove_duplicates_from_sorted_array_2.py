from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0   # write pointer

        for right in range(len(nums)):  # read pointer
            # keep first two occurrences of any value
            if left < 2 or nums[right] != nums[left - 2]:
                nums[left] = nums[right]
                left += 1

        return left
