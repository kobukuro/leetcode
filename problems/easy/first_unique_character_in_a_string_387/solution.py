# Tags: String, Hash Table
from collections import Counter


class Solution:
    # Time complexity: O(N) since we go through the string of length N two times.
    # Space complexity: O(1) because English alphabet contains 26 letters.
    def first_uniq_char(self, s: str) -> int:
        count = Counter(s)
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1
