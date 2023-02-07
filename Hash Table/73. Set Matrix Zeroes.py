# Array, Hash Table, Matrix
# reference:https://www.youtube.com/watch?v=T41rL0L3Pnw
# Time:O(m*n)
# Space:O(1)
class Solution:
    def setZeroes(self, matrix) -> None:
        # test cases
        # [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        # [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
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
