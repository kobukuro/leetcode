# Tags: DFS
from typing import List


class Solution:
    # m = # of rows, n = # of cols
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    def num_islands_dfs(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0

        def explore(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == '0' or (r, c) in visited:
                return False
            visited.add((r, c))
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c + 1)
            explore(r, c - 1)
            return True

        for r in range(rows):
            for c in range(cols):
                if explore(r, c):
                    res += 1
        return res
