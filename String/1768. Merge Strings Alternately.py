# String, Two Pointers
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = ''
        while i != len(word1) and j != len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1
        if i != len(word1):
            res += word1[i:]
        if j != len(word2):
            res += word2[j:]
        return res
