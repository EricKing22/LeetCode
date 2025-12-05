from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = [ [1] * len(matrix[0]) for _ in range(len(matrix))]

        elements = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                elements.append((i,j,matrix[i][j]))

        elements.sort(key = lambda x : x[-1], reverse=True)


        m = [0,0,1,-1]
        n = [1,-1,0,0]

        for node in elements:
            i,j, val = node
            for x,y in zip(m,n):
                ni = i + x
                nj = j + y
                if ni < 0 or nj < 0 or ni >= len(dp) or nj >= len(dp[0]):
                    pass

                elif matrix[ni][nj] < val:
                    dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)


        elements = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                elements.append((dp[i][j]))

        print(elements)
        elements.sort(reverse=True)
        return elements[0]


