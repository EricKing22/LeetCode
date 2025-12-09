from typing import List

class Solution:
    def __init__(self):
        self.ans = False
    def exist(self, board: List[List[str]], word: str) -> bool:


        def dfs(pos, k):
            y,x = pos
            if y < 0 or x < 0 or y > len(board) - 1 or x > len(board[0]) - 1:
                return

            if board[y][x] == word[k]:
                k += 1
            else:
                return

            if k == len(word):
                self.ans = True
                return

            xs = [0,0,1,-1]
            ys = [1,-1,0,0]

            for (xi,yi) in zip(xs,ys):
                temp = board[y][x]
                board[y][x] = "#"
                nx = x + xi
                ny = y + yi
                dfs((ny,nx), k)
                board[y][x] = temp

            k -= 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs((i,j),0)
                if self.ans:
                    return self.ans

        return self.ans