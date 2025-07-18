# Tags: DFS
from typing import List


class Solution:
    # Time complexity: O(R∗C), where R is the number of rows in the given grid, and C is the number of columns.
    # We visit every square once.
    # Space complexity: O(R∗C),
    # the space used by seen to keep track of visited squares and the space used by the call stack during our recursion.
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def explore(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            return 1 + explore(r + 1, c) + explore(r - 1, c) + explore(r, c + 1) + explore(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                res = max(res, explore(r, c))
        return res
