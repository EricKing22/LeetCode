
def trap(self, height) -> int:
    left = 0
    right = len(height)
    max_left = 0
    max_right = 0
    area = 0
    while (left < right):
        # update the index which has a higher potential to get the accurate answer
        if max_left < max_right:
            # update left
            left += 1
            max_left = max(max_left, height[left])
            area += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            area += max_right - height[right]

    return area