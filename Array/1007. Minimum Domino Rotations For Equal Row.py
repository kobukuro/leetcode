# Array, Greedy
import sys
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        hash_map = {}
        number_choices = set()
        i = 0
        for i in range(len(tops)):
            if len(number_choices) == 0:
                number_choices.add(tops[i])
                number_choices.add(bottoms[i])
                if tops[i] != bottoms[i]:
                    if tops[i] not in hash_map:
                        hash_map[tops[i]] = []
                        hash_map[tops[i]].append(1)
                        hash_map[tops[i]].append(0)
                    else:
                        hash_map[tops[i]][0] += 1
                    if bottoms[i] not in hash_map:
                        hash_map[bottoms[i]] = []
                        hash_map[bottoms[i]].append(0)
                        hash_map[bottoms[i]].append(1)
                    else:
                        hash_map[tops[i]][1] += 1
                else:
                    if tops[i] not in hash_map:
                        hash_map[tops[i]] = []
                        hash_map[tops[i]].append(0)
                        hash_map[tops[i]].append(0)
            else:
                if tops[i] not in number_choices and bottoms[i] not in number_choices:
                    return -1
                elif tops[i] in number_choices and bottoms[i] in number_choices:
                    number_choices = set()
                    number_choices.add(tops[i])
                    number_choices.add(bottoms[i])
                    if tops[i] != bottoms[i]:
                        hash_map[tops[i]][0] += 1
                        hash_map[bottoms[i]][1] += 1
                elif tops[i] in number_choices and bottoms[i] not in number_choices:
                    number_choices = set()
                    number_choices.add(tops[i])
                    hash_map = {k: v for k, v in hash_map.items() if k in number_choices}
                    if tops[i] not in hash_map:
                        hash_map[tops[i]] = []
                        hash_map[tops[i]].append(1)
                        hash_map[tops[i]].append(0)
                    else:
                        hash_map[tops[i]][0] += 1
                elif tops[i] not in number_choices and bottoms[i] in number_choices:
                    number_choices = set()
                    number_choices.add(bottoms[i])
                    hash_map = {k: v for k, v in hash_map.items() if k in number_choices}
                    if bottoms[i] not in hash_map:
                        hash_map[bottoms[i]] = []
                        hash_map[bottoms[i]].append(0)
                        hash_map[bottoms[i]].append(1)
                    else:
                        hash_map[bottoms[i]][1] += 1
        # print(hash_map)
        min_val = sys.maxsize
        for k, v in hash_map.items():
            if min(v) <= min_val:
                min_val = min(v)
        return min_val
