# Divide and Conquer, Bit Manipulation
# Time Complexity: O(1)
# Space Complexity: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) % 2
            res = res | bit << (31 - i)
        return res
