# Tags: Array, String
from typing import List


class Solution:
    def is_acronym(self, words: List[str], s: str) -> bool:
        """
        Time complexity: O(n)
        n represents the number of words in the words list
        Loop through words list and build acronym: O(n)
        String comparison acronym == s: Python short-circuits at first mismatch,
        worst case O(min(n, m)) where m = len(s)
        Since O(min(n, m)) ≤ O(n), overall time complexity is O(n)

        Space complexity: O(n)
        n represents the number of words in the words list
        acronym string is formed by taking first character of each word, length is n
        No other significant space usage
        """
        acronym = ''
        for word in words:
            acronym += word[0]
        return acronym == s
