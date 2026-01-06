from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            # if left part is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # if right part is sorted
            else:
                if nums[mid] < target <= nums[right-1]:
                    left = mid + 1
                else:
                    right = mid

        return -1