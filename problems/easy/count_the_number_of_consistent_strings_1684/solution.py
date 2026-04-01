# Tags: Array, String, Hash Table
from typing import List


class Solution:
    def count_consistent_strings(self, allowed: str, words: List[str]) -> int:
        """
        Let A be the length of allowed string, and L be the total number of characters across all words.

        Time complexity: O(A + L)
        - Creating the set from allowed: O(A)
        - Iterating through all words and characters: O(L) total
        - Each set lookup (c not in allowed_set) is O(1) on average
        - Overall: O(A) + O(L) = O(A + L)

        Space complexity: O(A)
        - The allowed_set set stores at most A unique characters from allowed
        - Other variables (res, is_consistent) use O(1) constant space
        - Overall: O(A)
        """
        allowed_set = set(allowed)
        res = 0
        for word in words:
            is_consistent = True
            for c in word:
                if c not in allowed_set:
                    is_consistent = False
                    break
            if is_consistent:
                res += 1
        return res
