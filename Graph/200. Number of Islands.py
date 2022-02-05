# Array, Depth-First Search, Breadth-First Search, Union Find, Matrix
# reference:https://www.youtube.com/watch?v=pV2kpPD66nE
from typing import List
from collections import deque


# bfs solution
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islands = 0
#
#         def bfs(r, c):
#             visited.add((r, c))
#             q = deque()
#             q.append((r, c))
#             while q:
#                 row, col = q.popleft()
#                 directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#                 for dr, dc in directions:
#                     r, c = row + dr, col + dc
#                     if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
#                         q.append((r, c))
#                         visited.add((r, c))
#
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1' and (r, c) not in visited:
#                     bfs(r, c)
#                     islands += 1
#         return islands

# dfs solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols:
                return False
            if (r, c) in visited:
                return False
            if grid[r][c] == '0':
                return False
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True

        res = 0
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col):
                    res += 1
        return res


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid=grid))
