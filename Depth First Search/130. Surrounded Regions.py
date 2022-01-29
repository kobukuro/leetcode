# Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
# reference:https://www.youtube.com/watch?v=9z2BunfoZ5Y
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'


if __name__ == '__main__':
    # board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    # board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    board = [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
    Solution().solve(board=board)
    print(board)
