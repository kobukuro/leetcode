# Dynamic Programming, Array, Depth-First Search
# reference:https://structy.net/problems/min-change
# reference:https://www.youtube.com/watch?v=jgiZlGzXMBw
from typing import List


# region brute force complexity analysis
# c:length of coins array, a:target amount
# Time:O(c^a), branching factor is based on the number of the coins,
# a will be the height of the tree
# Space:O(a), due to the call stack,
# and the height of the tree in worst case will be a(in worst case, use 1 cent coin all)
# endregion
# region memoization solution complexity analysis
# Time:O(a*c),
# Space:O(a) due to the call stack and we will store at most "a" different keys in memo hashmap
# endregion
class MemoizationSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def _coinChange(coins, amount, memo=None):
            if memo is None:
                memo = {}
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            min_val = float('inf')
            for coin in coins:
                val = 1 + _coinChange(coins, amount - coin, memo)
                min_val = min(min_val, val)
            memo[amount] = min_val
            return min_val

        ans = _coinChange(coins, amount)
        if ans == float('inf'):
            return -1
        else:
            return ans


# C:length of coins array, A:target amount
# Time:O(A*C), C work for A sub problems
# Space:O(A)
class DpSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[-1] if dp[-1] != amount + 1 else -1


if __name__ == '__main__':
    coins = [2]
    amount = 3
    print(MemoizationSolution().coinChange(coins=coins, amount=amount))
