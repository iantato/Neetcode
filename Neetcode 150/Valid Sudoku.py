'''

--- Neetcode 150 ---

Valid Sudoku
https://neetcode.io/problems/valid-sudoku

'''

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for y in range(0, 9):

            for x in range(0, 9):
                if board[y][x] == '.':
                    continue
                if board[y][x] in row[y] or board[y][x] in col[x] or board[y][x] in grid[(y // 3, x // 3)]:
                    return False

                row[y].add(board[y][x])
                col[x].add(board[y][x])
                grid[(y // 3, x // 3)].add(board[y][x])

        return True