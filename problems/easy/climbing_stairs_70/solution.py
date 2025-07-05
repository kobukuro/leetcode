# Tags: Memoization, Dynamic Programming
class Solution:
    # This solution will lead to a time limit exceeded error for larger inputs.
    # Time complexity : O(2^n). Because each node splits into two subtrees, and the height of the tree is n.
    # Space complexity : O(n). The depth of the recursion tree can go upto n.
    def climb_stairs_brute_force(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        return self.climb_stairs_brute_force(n - 1) + self.climb_stairs_brute_force(n - 2)

    # Time complexity : O(n). Size of recursion tree can go up to n.
    # Space complexity : O(n). The depth of the recursion tree can go up to n.
    def climb_stairs_memoization(self, n: int, memo=None) -> int:
        if memo is None:
            memo = {}
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in memo:
            return memo[n]
        memo[n] = self.climb_stairs_memoization(n - 1, memo) + self.climb_stairs_memoization(n - 2, memo)
        return memo[n]

    # Time complexity : O(n). Single loop up to n.
    # Space complexity : O(n). dp array of size n is used.
    def climb_stairs_dp(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
