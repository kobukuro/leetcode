# Array, Dynamic Programming, Matrix
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_edge = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = []
        for r in range(ROWS + 1):
            row = []
            for c in range(COLS + 1):
                row.append(0)
            dp.append(row)
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if matrix[r - 1][c - 1] == '1':
                    dp[r][c] = min(min(dp[r - 1][c], dp[r][c - 1]), dp[r - 1][c - 1]) + 1
                    max_edge = max(max_edge, dp[r][c])
        return max_edge * max_edge


class BetterSolution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_edge = 0
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [0] * (COLS + 1)
        prev = 0
        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                temp = dp[c]
                if matrix[r - 1][c - 1] == "1":
                    dp[c] = min(min(dp[c], dp[c - 1]), prev) + 1
                    max_edge = max(max_edge, dp[c])
                else:
                    dp[c] = 0
                prev = temp
        return max_edge * max_edge


if __name__ == "__main__":
    matrix = [["1", "1", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["0", "0", "0", "0", "0"],
              ["1", "1", "1", "1", "1"],
              ["1", "1", "1", "1", "1"]]
    print(Solution().maximalSquare(matrix))  # Output: 4
    print(BetterSolution().maximalSquare(matrix))  # Output: 4
