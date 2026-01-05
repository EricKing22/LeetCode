from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        d = deque() # store index
        ans = []
        for i,n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()

            d.append(i)

            if d[0] == i - k:
                d.popleft()

            if i >= k-1:
                ans.append(nums[d[0]])

        return ans



