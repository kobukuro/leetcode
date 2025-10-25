# Tags: Bit Manipulation, Divide and Conquer


class Solution:
    """
        Time complexity: O(1)
        Space complexity: O(1)
    """

    def hamming_weight(self, n: int) -> int:
        res = 0
        while n:
            if n % 2 == 1:
                res += 1
            n = n >> 1
        return res
