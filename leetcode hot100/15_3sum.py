from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []

        nums.sort()
        ans = set()

        for i in range(len(nums)-2):
            start = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = start + nums[left] + nums[right]

                if total == 0:
                    ans.add((start, nums[left], nums[right]))
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return [list(t) for t in list(ans)]
