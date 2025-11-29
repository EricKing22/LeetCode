import math
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window
        max_ans = 0

        left, right = 0, 0
        while right < len(nums):
            if nums[right] == 0:
                if k > 0:
                    right += 1
                    k -= 1
                else:
                    if nums[left] == 0:
                        k += 1
                    left += 1
            else:
                right += 1

            max_ans = max(max_ans, right - left)

        return max_ans


