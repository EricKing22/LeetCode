from typing import List

class Solution:
    def __init__(self):
        self.length_max = 0

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, (i,j), [(i,j)])

        return self.length_max

    def dfs(self, matrix, pos, way):

        i, j = pos
        current = matrix[i][j]

        top = matrix[max(0,i-1)][j]
        bottom = matrix[min(len(matrix)-1, i+1)][j]
        left = matrix[i][max(0,j-1)]
        right = matrix[i][min(len(matrix[0])-1, j+1)]

        if (top > current):
            new_pos = (max(0,i-1), j)
            way.append(new_pos)
            self.length_max = max(self.length_max, len(way))
            self.dfs(matrix, new_pos, way)

            way.pop()

        if left > current:
            new_pos = (i, max(0,j-1))
            way.append(new_pos)
            self.length_max = max(self.length_max, len(way))
            self.dfs(matrix, new_pos, way)

            way.pop()

        if right > current:
            new_pos = (i, min(len(matrix[0])-1, j+1))
            way.append(new_pos)
            self.length_max = max(self.length_max, len(way))
            self.dfs(matrix, new_pos, way)
            way.pop()

        if bottom > current:
            new_pos = (min(len(matrix)-1, i+1), j)
            way.append(new_pos)
            self.length_max = max(self.length_max, len(way))
            self.dfs(matrix, new_pos, way)
            way.pop()





