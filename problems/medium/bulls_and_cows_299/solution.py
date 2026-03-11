# Tags: String, Hash Table, Counting
from collections import Counter


class Solution:
    def get_hint(self, secret: str, guess: str) -> str:
        """
        Time complexity: O(n), where n is the length of secret/guess.
        We traverse the strings once to count bulls and build counters,
        then iterate through at most 10 digits (0-9) to count cows.

        Space complexity: O(1), counters store at most 10 digits (0-9).
        """
        bulls = 0
        cows = 0
        s_count = Counter()
        g_count = Counter()
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[s] += 1
                g_count[g] += 1
        for digit in s_count:
            cows += min(s_count[digit], g_count[digit])
        return f"{bulls}A{cows}B"
