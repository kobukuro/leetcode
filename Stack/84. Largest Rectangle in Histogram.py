# Array, Stack, Monotonic Stack
# reference:https://www.youtube.com/watch?v=zx5Sw9130L0
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, heights[0])]
        res = 0
        push_index = 0
        for i in range(1, len(heights)):
            ever_pop = False
            while stack:
                if stack[-1][1] > heights[i]:
                    res = max(res, (i - stack[-1][0]) * stack[-1][1])
                    push_index = stack[-1][0]
                    stack.pop()
                    ever_pop = True
                else:
                    if not ever_pop:
                        push_index = i
                    break
            stack.append((push_index, heights[i]))
        while stack:
            res = max(res, (len(heights) - stack[-1][0]) * stack[-1][1])
            stack.pop()
        # print(stack)
        return res


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights=heights))  # 10
