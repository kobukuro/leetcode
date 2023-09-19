from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for val in arr:
            count[val] += 1
        hash_set = set()
        for key, value in count.items():
            if value not in hash_set:
                hash_set.add(value)
            else:
                return False
        return True
