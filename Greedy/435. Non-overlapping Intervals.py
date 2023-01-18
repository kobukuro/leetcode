# Array, Dynamic Programming, Greedy, Sorting
from typing import List


# Time:(n log n)
# Space:O(log n)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        last_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < last_end:
                res += 1
                last_end = min(last_end, end)
            else:
                last_end = end
        return res
