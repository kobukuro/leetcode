# Dynamic Programming, DFS
# reference: https://www.youtube.com/watch?v=oBt53YbR9Kk&t=2319s
class Solution:
    # Time Limit Exceeded
    # Time complexity: O(2^(m+n))
    # Space complexity: O(m+n)
    def unique_paths_brute_force(self, m, n):
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return self.unique_paths_brute_force(m - 1, n) + self.unique_paths_brute_force(m, n - 1)

    # Time complexity: O(m*n)
    # Space complexity: O(m+n)
    def unique_paths_memoization(self, m, n, memo=None):
        key = (m, n)
        if memo is None:
            memo = {}
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        if key in memo:
            return memo[key]
        memo[key] = self.unique_paths_memoization(m - 1, n, memo) + self.unique_paths_memoization(m, n - 1, memo)
        return memo[key]

    # Time complexity: O(m*n)
    # Space complexity: O(m*n)
    def unique_paths_tabulation(self, m, n):
        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            dp.append(row)
        dp[1][1] = 1
        for i in range(m + 1):
            for j in range(n + 1):
                if i + 1 <= m:
                    dp[i + 1][j] += dp[i][j]
                if j + 1 <= n:
                    dp[i][j + 1] += dp[i][j]
        return dp[-1][-1]
