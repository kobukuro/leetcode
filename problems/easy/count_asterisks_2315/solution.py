# Tags: String
class Solution:
    def count_asterisks(self, s: str) -> int:
        """
        Count the number of asterisks (*) that are not between pairs of vertical bars (|).

        Args:
            s: Input string containing asterisks and vertical bars

        Returns:
            Number of asterisks outside of vertical bar pairs

        Time complexity: O(n) where n is the length of string s
        - split operation: O(n)
        - iterating through half of the words: O(n/2)
        - counting asterisks in words: O(n) total

        Space complexity: O(n) for the split result
        """
        words = s.split('|')
        res = 0
        for i in range(0, len(words), 2):
            res += words[i].count('*')
        return res
