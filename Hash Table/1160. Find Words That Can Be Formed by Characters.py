# Array, Hash Table, String
from typing import List
from collections import defaultdict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        chars_count = defaultdict(int)
        for ch in chars:
            chars_count[ch] += 1
        for word in words:
            is_good = True
            count = defaultdict(int)
            for w in word:
                count[w] += 1
            for key, value in count.items():
                if key not in chars_count:
                    is_good = False
                    break
                if value > chars_count[key]:
                    is_good = False
                    break
            if is_good:
                res += len(word)
        return res
