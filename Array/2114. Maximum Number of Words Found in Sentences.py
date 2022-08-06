# Array, String
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for sentence in sentences:
            length = len(sentence.split(' '))
            res = max(res, length)
        return res
