# Array, Sorting
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        compare = [-1, -1]
        total = len(intervals)
        remove_count = 0
        for interval in intervals:
            if interval[0] >= compare[0] and interval[1] <= compare[1]:
                remove_count += 1
            if interval[1] > compare[1]:
                if compare != [-1, -1] and compare[0] == interval[0]:
                    remove_count += 1
                compare = interval

        return total - remove_count


if __name__ == '__main__':
    intervals = [[1, 4], [3, 6], [2, 8]]
    print(Solution().removeCoveredIntervals(intervals=intervals))
    intervals = [[1, 4], [2, 3]]
    print(Solution().removeCoveredIntervals(intervals=intervals))
    intervals = [[1, 2], [1, 4], [3, 4]]
    print(Solution().removeCoveredIntervals(intervals=intervals))
