from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_dict = defaultdict(list)
        for src, dst in paths:
            paths_dict[src].append(dst)
        for key, values in paths_dict.items():
            for val in values:
                if val not in paths_dict:
                    return val
