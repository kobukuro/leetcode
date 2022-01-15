# Array, Hash Table, Matrix
# reference:https://www.youtube.com/watch?v=T41rL0L3Pnw
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        # 這個要最後
        if row_zero:
            for c in range(cols):
                matrix[0][c] = 0
