from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)

        area = 0

        while left < right:
            if height[left] < height[right]:
                area = max(area, (right - left) * min(height[left], height[right]))
                left += 1
            else:
                area = max(area, (right - left) * min(height[left], height[right]))
                right -= 1


        return area