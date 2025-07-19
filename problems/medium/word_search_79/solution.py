# Tags: Backtracking, DFS
from typing import List


class Solution:
    # w: length of word
    # Time complexity: O(m*n*4^w)
    # Space complexity: O(w)
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or board[r][c] != word[index]:
                return False
            visited.add((r, c))
            if dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or dfs(r, c + 1, index + 1) or dfs(r, c - 1,
                                                                                                       index + 1):
                return True
            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
