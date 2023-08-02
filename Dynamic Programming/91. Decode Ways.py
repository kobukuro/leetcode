# String, Dynamic Programming

# Time Complexity: O(N), where N is length of the string.
# Memoization helps in pruning the recursion tree and hence decoding for an index only once.
# Thus, this solution is linear time complexity.

# Space Complexity: O(N).
# The dictionary used for memoization would take the space equal to the length of the string.
# There would be an entry for each index value.
# The recursion stack would also be equal to the length of the string.
class BetterMemoizationSolution:
    def numDecodings(self, s: str) -> int:
        def can_decode(input_str):
            if input_str[0] == '0':
                return False
            if 1 <= int(input_str) <= 26:
                return True
            else:
                return False

        def dfs(s, start, memo=None):
            if memo is None:
                memo = {}
            if start in memo:
                return memo[start]
            if start == len(s):
                return 1
            val = 0
            for_end = start + 2 if len(s[start:]) == 1 else start + 3
            for end in range(start + 1, for_end):
                if can_decode(s[start:end]):
                    val += dfs(s, end, memo)
            memo[start] = val
            return memo[start]

        return dfs(s, 0)


# Time Complexity: O(N), where N is length of the string.
# We iterate the length of dp array which is N+1.
# Space Complexity: O(N). The length of the DP array.
class BetterTabulationSolution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for start in range(len(s) - 1, -1, -1):
            if s[start] == '0':
                continue
            dp[start] += dp[start + 1]
            if len(s[start:]) >= 2:
                if int(s[start:start + 2]) <= 26:
                    dp[start] += dp[start + 2]
        return dp[0]


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
