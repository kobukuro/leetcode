# String, Array
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(' ')
        res = ''
        for i in range(k):
            res += words[i]
            res += ' '
        return res[:-1]
