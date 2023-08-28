from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_chars = set(allowed)
        res = 0
        for word in words:
            is_consistent = True
            for c in word:
                if c not in set_chars:
                    is_consistent = False
                    break
            if is_consistent:
                res += 1
        return res
