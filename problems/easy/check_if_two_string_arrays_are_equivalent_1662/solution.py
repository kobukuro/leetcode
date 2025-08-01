# Tags: Array, String
from typing import List


class Solution:
    # Let N be the maximum of the number of all characters in word1 and the number of all characters in word2.
    # Time complexity: O(N), since we need to iterate over all characters in word1 and word2 to build the new strings.
    # Space complexity: O(N), since we need extra O(N) space to store the new built strings.
    def array_strings_are_equal(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
