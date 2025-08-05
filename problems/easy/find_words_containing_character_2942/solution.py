# Tags: Array, String
from typing import List


class Solution:
    # Let n be the length of the array and m be the length of the string.
    # Time complexity: O(n∗m).
    # We traverse each string to check if it contains the character x.

    # Space complexity: O(1).
    # The space required for the return variable is not included in the calculation.
    def find_words_containing(self, words: List[str], x: str) -> List[int]:
        res = []
        for i in range(len(words)):
            if x in words[i]:
                res.append(i)
        return res
