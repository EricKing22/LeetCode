from collections import defaultdict, Counter
from typing import List

# A good array is an array where the number of different integers in that array is exactly k.
class Solution:
    # Sliding Window Approach
    def slidingWindowAtMost(self, nums: List[int], k: int) -> int:
        left = 0


        mem = Counter() # key: num value: frequency

        total_count : int = 0
        for right in range(len(nums)):
            mem[nums[right]] += 1
            while len(mem) > k:
                mem[nums[left]] -= 1
                if mem[nums[left]] == 0: mem.pop(nums[left])
                left += 1




            total_count = total_count + right - left + 1

        return  total_count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.slidingWindowAtMost(nums,k) - self.slidingWindowAtMost(nums,k-1)






s = Solution()
print(s.subarraysWithKDistinct([1,2,1,2,3], 2))





