import math
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = math.ceil((left + right) / 2)

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return True if target in matrix[mid] else False

            if matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1

        return False