from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num < 2:
            return True

        left = 0
        right = num

        while left < right:
            mid = left + (right - left) // 2

            if mid ** 2 == num:
                return True

            if mid ** 2 > num:
                right = mid
            else:
                left = mid + 1

        return False