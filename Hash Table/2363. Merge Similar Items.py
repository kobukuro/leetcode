from typing import List
from collections import defaultdict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mapping = defaultdict(int)
        for val, weight in items1:
            mapping[val] += weight
        for val, weight in items2:
            mapping[val] += weight
        res = []
        for key, value in mapping.items():
            res.append([key, value])
        res.sort()
        return res
