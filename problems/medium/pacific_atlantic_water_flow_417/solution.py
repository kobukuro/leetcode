# Tags: DFS
from typing import List


class Solution:
    # Time complexity: O(M*N),
    # where M is the number of rows and N is the number of columns.
    # The dfs function runs exactly once for each cell accessible from an ocean.

    # Space complexity: O(M*N),
    # where M is the number of rows and N is the number of columns.
    # Space is occupied by dfs calls on the recursion stack.
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if r < 0 or r == rows or c < 0 or c == cols \
                    or heights[r][c] < prev_height or (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
