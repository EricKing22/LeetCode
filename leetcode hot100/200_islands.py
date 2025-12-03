from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0

        def dfs(i,j,):
            if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1"):
                return


            grid[i][j] = "#"

            ni = [0,0,1,-1]
            nj = [-1,1,0,0]

            for x in range(4):
                dfs(i + ni[x], j + nj[x])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    num_islands += 1
                    dfs(i,j)

        return num_islands
