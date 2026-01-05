from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        ans = 0

        def dfs(i,j):

            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] != "1":
                return

            grid[i][j] = "#"

            xs = [0,1,0,-1]
            ys = [1,0,-1,0]

            for nx, ny in zip(xs,ys):
                dfs(i+nx, j+ny)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)

        return ans
