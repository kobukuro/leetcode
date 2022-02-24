# Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
# reference:https://www.youtube.com/watch?v=2Yk3Avrzauk
# reference:https://www.youtube.com/watch?v=zx5Sw9130L0
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            maxArea = 0
            stack = []  # pair: (index, height)

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start, h))

            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))
            return maxArea

        def produce_histogram(matrix):
            res = []
            rows = len(matrix)
            cols = len(matrix[0])
            for row in range(rows):
                res_inside = []
                for col in range(cols):
                    if matrix[row][col] == '0':
                        res_inside.append(0)
                    else:
                        num = 1
                        r = row - 1
                        finished = False
                        while r >= 0:
                            if matrix[r][col] == '1':
                                num += 1
                            else:
                                res_inside.append(num)
                                finished = True
                                break
                            r -= 1
                        if not finished:
                            res_inside.append(num)
                res.append(res_inside)
            return res

        histograms = produce_histogram(matrix=matrix)
        res = 0
        for histogram in histograms:
            res = max(res, largestRectangleArea(histogram))
        return res


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalRectangle(matrix=matrix))
