# String, Dynamic Programming
class MemoizationSolution:
    def numDecodings(self, s: str) -> int:
        candidates = []
        for i in range(1, 27):
            candidates.append(str(i))

        # print(candidates)
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


class TabulationSolution:
    def numDecodings(self, s: str) -> int:
        candidates = []
        for i in range(1, 27):
            candidates.append(str(i))
        dp = [0] * (len(s) + 1)
        # print(dp)
        dp[-1] = 1
        for start in range(len(s) - 1, -1, -1):
            for candidate in candidates:
                if start + len(candidate) <= len(s) and s[start:start + len(candidate)] == candidate:
                    dp[start] += dp[start + len(candidate)]
        return dp[0]
