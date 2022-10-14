# Hash Table, String
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        indices = {}
        i = 0
        for key in keyboard:
            indices[key] = i
            i += 1
        res = 0
        curr = 0
        for i in range(len(word)):
            res += abs(curr - indices[word[i]])
            curr = indices[word[i]]
        return res
