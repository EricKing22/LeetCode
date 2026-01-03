from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target_color = image[sr][sc]

        if target_color == color:
            return image

        def dfs(current_x, current_y):
            print(current_y, current_x)
            if current_y < 0 or current_y > len(image)-1 or current_x < 0 or current_x > len(image[0])-1:
                return

            if image[current_y][current_x] != target_color:
                return

            image[current_y][current_x] = color

            xs = [1,0,-1,0]
            ys = [0,1,0,-1]

            for nx,ny in zip(xs,ys):
                dfs(current_x+nx,current_y+ny)

        dfs(sc,sr)

        return image