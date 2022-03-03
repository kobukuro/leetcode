# Dynamic Programming, Bit Manipulation
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append("{0:b}".format(i).count('1'))
        return ans


if __name__ == '__main__':
    print(Solution().countBits(n=2))
