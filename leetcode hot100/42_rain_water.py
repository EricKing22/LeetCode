from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[right]
        area = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                area += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                area += right_max - height[right]

        return area