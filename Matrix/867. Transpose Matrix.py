# Array, Matrix, Simulation
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        for c in range(COLS):
            row = []
            for r in range(ROWS):
                row.append(matrix[r][c])
            res.append(row)
        return res
