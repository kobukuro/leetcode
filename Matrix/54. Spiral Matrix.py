# Array, Matrix, Simulation
from typing import List
import enum


@enum.unique
class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4


# Let M be the number of rows and N be the number of columns.
# Time complexity: O(M⋅N)
# Space complexity: O(M⋅N) because of hash set(visited variable)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        count = 0
        total_num = len(matrix) * len(matrix[0])
        r, c = 0, 0
        visited = set()
        direction = Direction.RIGHT.value
        while count < total_num:
            if c == len(matrix[0]):
                r += 1
                c -= 1
                direction = Direction.DOWN.value
            elif c == -1:
                r -= 1
                c += 1
                direction = Direction.UP.value
            elif r == len(matrix):
                r -= 1
                c -= 1
                direction = Direction.LEFT.value
            elif r == -1:
                r += 1
                c += 1
                direction = Direction.RIGHT.value
            if (r, c) in visited:
                if direction == Direction.UP.value:
                    r += 1
                    c += 1
                    direction = Direction.RIGHT.value
                elif direction == Direction.RIGHT.value:
                    r += 1
                    c -= 1
                    direction = Direction.DOWN.value
                elif direction == Direction.DOWN.value:
                    r -= 1
                    c -= 1
                    direction = Direction.LEFT.value
                elif direction == Direction.LEFT.value:
                    r -= 1
                    c += 1
                    direction = Direction.UP.value
            visited.add((r, c))
            count += 1
            res.append(matrix[r][c])
            if direction == Direction.RIGHT.value:
                c += 1
            elif direction == Direction.UP.value:
                r -= 1
            elif direction == Direction.LEFT.value:
                c -= 1
            elif direction == Direction.DOWN.value:
                r += 1
        return res


class SimplifiedSolution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        direction = Direction.RIGHT.value
        ROWS = len(matrix)
        COLS = len(matrix[0])
        total_count = ROWS * COLS
        curr_count = 0
        r = c = 0
        while curr_count < total_count:
            if c == COLS or ((r, c) in visited and direction == Direction.RIGHT.value):
                c -= 1
                r += 1
                direction = Direction.DOWN.value
            elif r == ROWS or ((r, c) in visited and direction == Direction.DOWN.value):
                r -= 1
                c -= 1
                direction = Direction.LEFT.value
            elif c < 0 or ((r, c) in visited and direction == Direction.LEFT.value):
                r -= 1
                c += 1
                direction = Direction.UP.value
            elif r < 0 or ((r, c) in visited and direction == Direction.UP.value):
                r += 1
                c += 1
                direction = Direction.RIGHT.value
            visited.add((r, c))
            res.append(matrix[r][c])
            curr_count += 1
            if direction == Direction.RIGHT.value:
                c += 1
            elif direction == Direction.DOWN.value:
                r += 1
            elif direction == Direction.LEFT.value:
                c -= 1
            elif direction == Direction.UP.value:
                r -= 1
        return res
