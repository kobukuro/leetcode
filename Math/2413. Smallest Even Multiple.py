# Math, Number Theory
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n == 1:
            return 2
        if n % 2 != 0:
            return 2 * n
        return max(2, n)
