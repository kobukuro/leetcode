# Tags: Array, String, Hash Table
from typing import List
from collections import defaultdict


class Solution:
    # Given n as the length of chars, m as the length of words and k as the average length of each word in words
    # Time complexity: O(n + m * k)
    # To calculate chars_count, we iterate over each character of chars once, costing O(n).
    # Next, we iterate over O(m) elements in words.
    # For each element, we calculate word_count by iterating over the element, which costs O(k).
    # We then iterate over word_count.
    # As the input only contains lowercase English letters,
    # this costs O(1) since word_count cannot have a length greater than 26.
    # Overall, the for loop costs O(m⋅k).

    # Space complexity: O(1)
    # We use extra space for chars_count and word_count.
    # However, the input only contains lowercase English letters.
    # Thus, the size of these dictionaries never exceed 26, so we use O(1) space.
    def count_characters(self, words: List[str], chars: str) -> int:
        res = 0
        chars_count = defaultdict(int)
        for c in chars:
            chars_count[c] += 1
        for word in words:
            word_count = defaultdict(int)
            is_good = True
            for c in word:
                word_count[c] += 1
                if word_count[c] > chars_count[c]:
                    is_good = False
                    break
            if is_good:
                res += len(word)
        return res
