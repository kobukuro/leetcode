# Array, Stack, Simulation
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        stack = []
        while i < len(pushed) and j < len(popped):
            stack.append(pushed[i])
            i += 1
            while stack:
                if stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    break
        return True if not stack else False


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(Solution().validateStackSequences(pushed=pushed, popped=popped))
