# Tags: DFS, Dynamic Programming
# references:
# 1. https://structy.net/problems/min-change
# 2. https://www.youtube.com/watch?v=jgiZlGzXMBw
from typing import List


class Solution:
    # Time Limit Exceeded
    # C: length of coins array, A: target amount
    # Time complexity: O(C^A), branching factor is based on the number of the coins,
    # "A" will be the height of the tree

    # Space complexity: O(A), due to the call stack,
    # then the height of the tree in worst case will be A(in worst case, use 1 cent coin all)
    def coin_change_brute_force(self, coins: List[int], amount: int) -> int:
        def _coin_change(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            min_val = float('inf')
            for coin in coins:
                min_val = min(min_val, _coin_change(coins, amount - coin))
            return 1 + min_val

        ans = _coin_change(coins, amount)
        return ans if ans != float('inf') else -1

    # Time complexity: O(A*C),
    # Space complexity: O(A) due to the call stack, and we will store at most "A" different keys in memo hashmap
    def coin_change_memoization(self, coins: List[int], amount: int) -> int:
        def _coin_change(coins, amount, memo=None):
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
                min_val = min(min_val, _coin_change(coins, amount - coin, memo))
            memo[amount] = 1 + min_val
            return memo[amount]

        ans = _coin_change(coins, amount)
        return ans if ans != float('inf') else -1

    # C:length of coins array, A:target amount
    # Time complexity: O(A*C), C work for A sub problems
    # Space complexity: O(A)
    def coin_change_dp(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[-1] if dp[-1] != amount + 1 else -1
