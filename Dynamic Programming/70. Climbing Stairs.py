# Math, Dynamic Programming, Memoization

# Brute Force
# Time:O(2^n), 因為每個節點都會有兩個分支, 然後樹的高度為n
# Space:O(n). The depth of the recursion tree can go upto n.

# Time:O(n), O(2n) -> O(n)
# Space:O(n)
class MemoizationSolution:
    def climbStairs(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]


# Time:O(n)
# Space:O(n)
class TabulationSolution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
