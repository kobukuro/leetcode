class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        val = 0
        for i in range(1, n + 1):
            val += 1
            if i != 1 and i % 7 == 1:
                val -= 6
            res += val
        return res
