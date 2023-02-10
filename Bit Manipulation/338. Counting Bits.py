# Dynamic Programming, Bit Manipulation
from typing import List


# Time complexity: O(n).
# For each integer x, in the range 1 to n,
# we need to perform a constant number of operations which does not depend on the number of bits in x.
# Space complexity: O(1).
# Since the output array does not count towards the space complexity.
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


class SlowSolution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            ans.append("{0:b}".format(i).count('1'))
        return ans


if __name__ == '__main__':
    print(Solution().countBits(n=2))
