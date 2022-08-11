# String, Dynamic Programming

# n is the length of the input string.
# Time complexity : O(n^3).
# first n is the recursion (we keep track of how many times word break is being called),
# second n is the for loop
# (we keep track of how many for loop iterations each one of those calls is making),
# and third n is due to substring.
# Space complexity : O(n). The depth of recursion tree can go up to n.
# we already have a cache size of N
# and the recursive stack in the worst case is always going to go at a maximum of size N.
class MemoizationSolution:
    def numDecodings(self, s: str) -> int:
        candidates = []
        for i in range(1, 27):
            candidates.append(str(i))

        def dfs(start, memo=None):
            if memo is None:
                memo = {}
            if start in memo:
                return memo[start]
            if start == len(s):
                return 1
            val = 0
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in candidates:
                    val += dfs(end, memo)
            memo[start] = val
            return memo[start]

        return dfs(0)


# n is the length of the input string.
# Time complexity : O(n^3).
# There are two nested loops, and substring computation at each iteration.
# Overall that results in O(n^3) time complexity.
# Space complexity : O(n). Length of dp array is n+1.
class TabulationSolution:
    def numDecodings(self, s: str) -> int:
        candidates = []
        for i in range(1, 27):
            candidates.append(str(i))
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for start in range(len(s) - 1, -1, -1):
            for candidate in candidates:
                if start + len(candidate) <= len(s) and s[start:start + len(candidate)] == candidate:
                    dp[start] += dp[start + len(candidate)]
        return dp[0]
