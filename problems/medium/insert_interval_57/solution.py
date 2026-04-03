# Tags: Array
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Insert new_interval into sorted intervals and merge overlapping intervals.

        Args:
            intervals: List of non-overlapping intervals sorted by start time.
                       Each interval is [start, end] where start <= end.
            new_interval: The interval to insert, formatted as [start, end].

        Returns:
            List of non-overlapping intervals sorted by start time after insertion
            and merging all overlapping intervals.

        Time Complexity: O(n)
        - Single pass through intervals list where n = len(intervals)
        - Each iteration performs O(1) operations (comparisons, min/max)
        - Worst case: process all intervals before finding insertion point

        Space Complexity: O(1) auxiliary space (excluding output)
        - Only uses constant extra variables for iteration (i)
        - Output list 'res' is not counted as auxiliary space
        """
        res = []
        for i in range(len(intervals)):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                return res + intervals[i:]
            elif new_interval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                new_interval = [min(new_interval[0], intervals[i][0]),
                                max(new_interval[1], intervals[i][1])]
        res.append(new_interval)
        return res
