from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 1
        min_len = 1e6
        sub_sum = nums[0]
        while right <= len(nums):
            if left == len(nums):
                break

            if left == right:
                right = left + 1

            if sub_sum >= target:
                min_len = min(min_len, right - left)
                sub_sum -= nums[left]
                left += 1
            else:
                if right == len(nums):
                    break
                sub_sum += nums[right]
                right += 1

        return 0 if min_len == 1e6 else min_len