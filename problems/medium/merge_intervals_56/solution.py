# Tags: Array, Sorting
from typing import List


class Solution:
    # Time complexity : O(n log n)
    # Other than the sort invocation, we do a simple linear scan of the list,
    # so the runtime is dominated by the O(n log n) complexity of sorting.
    # Space complexity : O(logN) (or O(n))
    # If we can sort intervals in place, we do not need more than constant additional space,
    # although the sorting itself takes O(log n) space.
    # Otherwise, we must allocate linear space to store a copy of intervals and sort that.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last_interval = res[-1]
            current_interval = intervals[i]
            if current_interval[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], current_interval[1])
            else:
                res.append(current_interval)
        return res
