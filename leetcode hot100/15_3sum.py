from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = set()

        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return list(ans)


