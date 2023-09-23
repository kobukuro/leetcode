from typing import List
from collections import defaultdict


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        for word in words:
            count = defaultdict(int)
            for c in word:
                c = c.lower()
                if c in first:
                    count[1] += 1
                if c in second:
                    count[2] += 1
                if c in third:
                    count[3] += 1
            if len(count.keys()) == 1:
                res.append(word)
        return res
