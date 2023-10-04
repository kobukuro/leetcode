class Solution:
    def countAsterisks(self, s: str) -> int:
        words = s.split('|')
        res = 0
        for i in range(0, len(words), 2):
            res += words[i].count('*')
        return res
