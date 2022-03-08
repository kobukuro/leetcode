# Math, Dynamic Programming, Combinatorics
# reference:https://www.youtube.com/watch?v=_OKIln4iieM
from itertools import permutations


class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        modulo = 1000000007
        for i in range(1, n + 1):
            res *= i
            res %= modulo
            res *= (2 * i - 1)
            res %= modulo
        return res % modulo


if __name__ == '__main__':
    n = 3
    print(Solution().countOrders(n=n))
