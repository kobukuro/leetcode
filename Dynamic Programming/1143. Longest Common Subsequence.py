# String, Dynamic Programming
# Time complexity : O(M*N).
# There are M possible positions for the first string, and N for the second string.
# Solving each subproblem has a cost of O(1).
# Again, there are M*N subproblems, and so we get a total time complexity of O(M*N).

# Space complexity : O(M*N).
# We need to store the answer for each of the M*N subproblems.
class MemoizationSolution:
    def longestCommonSubsequence(self, text1: str, text2: str, memo=None) -> int:
        if memo is None:
            memo = {}
        key = (text1, text2)
        if text1 == '' or text2 == '':
            return 0
        if key in memo:
            return memo[key]
        last_letter1 = text1[-1]
        last_letter2 = text2[-1]
        if last_letter1 == last_letter2:
            value1 = 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1], memo)
            memo[key] = value1
            return memo[key]
        else:
            value2 = max(self.longestCommonSubsequence(text1[:-1], text2, memo),
                         self.longestCommonSubsequence(text1, text2[:-1], memo))
            memo[key] = value2
            return memo[key]


# Time complexity : O(M*N).
# We're solving M*N subproblems. Solving each subproblem is an O(1) operation.

# Space complexity : O(M*N).
# We'e allocating a 2D array of size M*N to save the answers to subproblems.
class TabulationSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for j in range(len(text2) + 1):
            temp = []
            for i in range(len(text1) + 1):
                temp.append(0)
            dp.append(temp)
        # print(dp)
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print(dp)
        return dp[-1][-1]
