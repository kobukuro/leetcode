# Tags: String, Hash Table
from collections import defaultdict


class Solution:
    # We'll say m is the length of the magazine, and n is the length of the ransom note.
    # Also, let k be the number of unique characters across both the ransom note and magazine.
    # While this is never more than 26, we'll treat it as a variable for a more accurate complexity analysis.
    # The basic dictionary operations, get(...) and put(...), are O(1) time complexity.

    # Time complexity : O(m).
    # When m<n, we immediately return false. Therefore, the worst case occurs when m≥n.
    # Creating a dictionary of counts for the magazine is O(m),
    # as each insertion/ count update is O(1), and is done for each of the m characters.
    # Likewise, creating the dictionary of counts for the ransom note is O(n).
    # We then iterate over the ransom note dictionary,
    # which contains at most n unique values, looking up their counterparts in the magazine dictionary.
    # This is, therefore, at worst O(n).
    # This gives us O(n)+O(n)+O(m). Now, remember how we said m≥n?
    # This means that we can simplify it to O(m)+O(m)+O(m)=3⋅O(m)=O(m), dropping the constant of 3.

    # Space Complexity : O(k) / O(1).
    # We build two dictionaries of counts; each with up to k characters in them.
    # This means that they take up O(k) space.
    # For this problem, because k is never more than 26, which is a constant,
    # it'd be reasonable to say that this algorithm requires O(1) space.
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        if len(ransom_note) > len(magazine):
            return False
        ransom_char_count = defaultdict(int)
        for char in ransom_note:
            ransom_char_count[char] += 1
        magazine_char_count = defaultdict(int)
        for char in magazine:
            magazine_char_count[char] += 1
        for char, count in ransom_char_count.items():
            if magazine_char_count[char] < count:
                return False
        return True
