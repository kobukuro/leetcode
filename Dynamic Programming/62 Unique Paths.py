# Dynamic Programming, Math, Combinatorics
class Solution:
    def uniquePaths(self, m, n, memo=None):
        if memo is None:
            memo = {}
        key = (m, n)
        if key in memo:
            return memo[key]
        if m == 1 or n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        memo[key] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return memo[key]


if __name__ == '__main__':
    print(Solution().uniquePaths(m=7, n=3))
