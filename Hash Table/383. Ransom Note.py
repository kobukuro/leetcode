# Hash Table, String, Counting
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r = defaultdict(int)
        for c in ransomNote:
            count_r[c] += 1
        count_m = defaultdict(int)
        for c in magazine:
            count_m[c] += 1
        for key, value in count_r.items():
            if count_m[key] < value:
                return False
        return True
