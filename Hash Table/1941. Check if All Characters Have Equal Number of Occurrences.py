from collections import defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        return len(set(count.values())) == 1
