# Dynamic Programming, Depth-First Search, Breadth-First Search, Graph, Topological Sort, Memoization
# reference:https://www.youtube.com/watch?v=wCc_nd-GiEc
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        hash_map = {}

        def dfs(r, c, preVal):
            if r >= ROWS or r < 0 or c < 0 or c >= COLS or matrix[r][c] <= preVal:
                return 0
            if (r, c) in hash_map:
                return hash_map[(r, c)]
            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            hash_map[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(hash_map.values())


if __name__ == '__main__':
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print(Solution().longestIncreasingPath(matrix=matrix))
