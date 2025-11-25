from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        x, y, dx, dy = 0, 0, 1, 0
        for _ in range(len(matrix) * len(matrix[0])):
            ans.append(matrix[y][x])
            matrix[y][x] = "#"

            # Spiral rotation
            if x + dx < 0 or x + dx > len(matrix[0])-1 or y + dy < 0 or y + dy > len(matrix)-1 or matrix[y+dy][x+dx] == "#":
                dx, dy = -dy, dx

            x += dx
            y += dy

        return ans



