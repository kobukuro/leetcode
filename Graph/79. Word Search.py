# Array ,Backtracking, Matrix
from typing import List


# w:length of word
# Time Complexity:O(m*n*4^w)
# Space Complexity:O(w)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        COLS = len(board[0])
        ROWS = len(board)
        len_word = len(word)
        visited = set()

        def dfs(row, col, index):
            if index == len_word:
                return True
            if row < 0 or row == ROWS or col < 0 or col == COLS \
                    or (row, col) in visited or board[row][col] != word[index]:
                return False
            visited.add((row, col))
            if dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) \
                    or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1):
                return True
            visited.remove((row, col))
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False
