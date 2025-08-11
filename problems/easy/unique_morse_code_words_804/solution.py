# Tags: Array, String, Hash Table
from typing import List


class Solution:
    # Time complexity: O(S),
    # where S is the sum of the lengths of words in words.
    # We iterate through each character of each word in words.

    # Space complexity: O(S).
    def unique_morse_representations(self, words: List[str]) -> int:
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        hash_set = set()
        for word in words:
            morse_chars = []
            for c in word:
                morse_chars.append(codes[ord(c) - ord("a")])
            hash_set.add(''.join(morse_chars))
        return len(hash_set)
