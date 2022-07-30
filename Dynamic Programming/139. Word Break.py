# Dynamic Programming, Memoization, String, Hash Table, Trie
from typing import List


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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s, set_words, start, memo=None):
            if memo is None:
                memo = {}
            if start in memo:
                return memo[start]
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in set_words and dfs(s, set_words, end, memo):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return dfs(s, set(wordDict), 0)


# n is the length of the input string.
# Time complexity : O(n^3).
# There are two nested loops, and substring computation at each iteration.
# Overall that results in O(n^3) time complexity.
# Space complexity : O(n). Length of dp array is n+1.
class TabulationSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for start in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if start + len(word) <= len(s) and s[start:start + len(word)] == word:
                    dp[start] = dp[start + len(word)]
                if dp[start]:
                    break
        return dp[0]
