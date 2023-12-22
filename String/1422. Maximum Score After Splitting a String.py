# String
class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1):
            score = s[:i + 1].count('0') + s[i + 1:].count('1')
            res = max(res, score)
        return res
