# Tags: Array, String
from typing import List


class Solution:
    def prefix_count(self, words: List[str], pref: str) -> int:
        """
        Count how many words in the list start with the given prefix.

        Args:
            words: List of words to check
            pref: The prefix string to search for

        Returns:
            The number of words that start with the given prefix

        Time complexity: O(n × m) where n is the number of words and m is the prefix length
        - Each word's startswith() check: O(m) in the worst case
        - Checking all n words: O(n × m)

        Space complexity: O(1) auxiliary space
        - Only uses a counter variable 'res'
        """
        res = 0
        for word in words:
            if word.startswith(pref):
                res += 1
        return res
