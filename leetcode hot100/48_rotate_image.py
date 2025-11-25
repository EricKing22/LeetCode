from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # rotation = flip by horizontal line + transpose

        # vertical flip
        top = 0
        bottom = len(matrix)-1
        while top < bottom:
            temp = matrix[top]
            matrix[top] = matrix[bottom]
            matrix[bottom] = temp
            top += 1
            bottom -= 1

        # transpose

        ans = [ [ row[i] for row in matrix] for i in range(len(matrix))]
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                matrix[i][j] = ans[i][j]





