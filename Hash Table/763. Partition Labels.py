# Hash Table, Two Pointers, String, Greedy
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapping = {}
        for i, ele in enumerate(s):
            if ele not in mapping:
                mapping[ele] = [i, i]
            else:
                mapping[ele][1] = i
        print(mapping)
        # 0, 8
        # 9, 14
        intervals = []
        for k, v in mapping.items():
            if not intervals:
                intervals.append(v)
            else:
                modified = False
                no_append = False
                for interval in intervals:
                    if interval[0] < v[0] and interval[1] > v[0] and v[1] > interval[1]:
                        interval[1] = v[1]
                        modified = True
                        break
                    elif v[0] > interval[0] and v[1] < interval[1]:
                        no_append = True
                if not modified and not no_append:
                    intervals.append([v[0], v[1]])
        print(intervals)
        ans = []
        for interval in intervals:
            ans.append(interval[1] - interval[0] + 1)
        return ans
