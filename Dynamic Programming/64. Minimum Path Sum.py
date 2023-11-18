from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dp = []
        for r in range(ROWS + 1):
            row = []
            for c in range(COLS + 1):
                row.append(float('inf'))
            dp.append(row)
        dp[-1][COLS - 1] = 0
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = min(dp[r + 1][c], dp[r][c + 1]) + grid[r][c]
        return dp[0][0]
