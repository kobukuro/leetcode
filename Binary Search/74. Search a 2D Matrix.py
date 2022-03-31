# Array, Binary Search, Matrix
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        print(m, n)
        left = 0
        right = m * n - 1
        while left <= right:
            pivot_index = left + (right - left) // 2
            pivot_ele = matrix[pivot_index // n][pivot_index % n]
            if pivot_ele == target:
                return True
            elif target < pivot_ele:
                right = pivot_index - 1
            else:
                left = pivot_index + 1
        return False
