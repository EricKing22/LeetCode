from typing import List


class Solution:


    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        ans = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1

                while num + length in nums:
                    length += 1

                ans = max(ans, length)

        return ans
