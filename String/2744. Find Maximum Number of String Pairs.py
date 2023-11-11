from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        words_set = set(words)
        res_set = set()
        res = 0
        for word in words:
            if word in res_set or (word[0] == word[1]):
                continue
            else:
                reversed_word = word[::-1]
                if reversed_word in words_set:
                    res += 1
                    res_set.add(word)
                    res_set.add(reversed_word)
        return res
