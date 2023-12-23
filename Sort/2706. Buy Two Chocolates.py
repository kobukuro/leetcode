from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        leftover = money - prices[0] - prices[1]
        return money if leftover < 0 else leftover
