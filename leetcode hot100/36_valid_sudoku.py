from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def is_valid(row):
            for i in range(9):
                if row[i] != "." and row[i] in row[i + 1:]:
                    return False
            return True

        ans = True

        for row in board:
            ans = ans and is_valid(row)

        print("After row check: ", ans)

        # col check
        cols = [[row[i] for row in board] for i in range(9)]
        for col in cols:
            ans = ans and is_valid(col)
        print("After col check: ", ans)

        squares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = []
                square.append(board[i][j])
                square.append(board[i + 1][j])
                square.append(board[i + 2][j])
                square.append(board[i][j + 1])
                square.append(board[i + 1][j + 1])
                square.append(board[i + 2][j + 1])
                square.append(board[i][j + 2])
                square.append(board[i + 1][j + 2])
                square.append(board[i + 2][j + 2])
                squares.append(square)

        print("squares", squares)

        for square in squares:
            ans = ans and is_valid((square))

        return ans
