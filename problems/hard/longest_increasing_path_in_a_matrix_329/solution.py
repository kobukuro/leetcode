# Tags: Matrix, DFS, Dynamic Programming, Graph
from typing import List


class Solution:
    # Time complexity: O(mn).
    # Each vertex/cell will be calculated once and only once,
    # and each edge will be visited once and only once.
    # The total time complexity is then O(V+E).
    # V is the total number of vertices and E is the total number of edges.
    # In our problem, O(V)=O(mn), O(E)=O(4V)=O(mn).

    # Space complexity: O(mn). The cache dominates the space complexity.
    def longest_increasing_path(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {}
        res = 0

        def dfs(r, c, prev_val):
            if r < 0 or r == rows or c < 0 or c == cols or matrix[r][c] <= prev_val:
                return 0
            key = (r, c)
            if key in memo:
                return memo[key]
            memo[key] = 1 + max(dfs(r + 1, c, matrix[r][c]),
                                dfs(r - 1, c, matrix[r][c]),
                                dfs(r, c + 1, matrix[r][c]),
                                dfs(r, c - 1, matrix[r][c]))
            return memo[key]

        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, -1))
        return res
