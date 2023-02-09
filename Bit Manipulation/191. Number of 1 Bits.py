# Divide and Conquer, Bit Manipulation
# Time complexity: O(1)
# Space complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n = n >> 1
        return res


class SlowSolution:
    def hammingWeight(self, n: int) -> int:
        power_limit = 0
        value = 0
        while value < n:
            value = pow(2, power_limit)
            power_limit += 1
        # print(power_limit, value)
        # print(n)
        res = 0
        for i in range(power_limit - 1, -1, -1):
            if pow(2, i) <= n:
                # print(i)
                res += 1
                n -= pow(2, i)
        return res
