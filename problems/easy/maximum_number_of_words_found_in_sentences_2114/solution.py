# Tags: Array, String
from typing import List


class Solution:
    def most_words_found(self, sentences: List[str]) -> int:
        """
        Find the maximum number of words in any sentence.

        Args:
            sentences: List of sentences (strings)

        Returns:
            The maximum number of words found in any single sentence

        Time complexity: O(n × m) where n is the number of sentences and m is the average sentence length
        - Iterate through each sentence: O(n)
        - Each split() operation creates a list of words: O(m) per sentence
        - Total: O(n × m) in the worst case

        Space complexity: O(m) for the split result, O(1) auxiliary space
        - O(m) for the temporary list created by split()
        - O(1) additional space for the 'res' variable
        """
        res = 0
        for sentence in sentences:
            res = max(res, len(sentence.split()))
        return res
