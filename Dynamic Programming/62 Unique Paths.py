# Dynamic Programming, Math, Combinatorics
# reference:https://www.youtube.com/watch?v=oBt53YbR9Kk&t=2319s

# Time Limit Exceeded
# Time:O(2^(m+n))
# Space:O(m+n)
class BruteForceSolution:
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


# Time:O(m*n)
# Space:O(m+n)
class MemoizationSolution:
    def uniquePaths(self, m, n, memo=None):
        key = (m, n)
        if memo is None:
            memo = {}
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        if key in memo:
            return memo[key]
        memo[key] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)
        return memo[key]


# Time:O(m*n)
# Space:O(m*n)
class TabulationSolution:
    def uniquePaths(self, m, n):
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


if __name__ == '__main__':
    print(MemoizationSolution().uniquePaths(m=18, n=18))
