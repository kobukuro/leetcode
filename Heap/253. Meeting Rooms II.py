# Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum
from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        zooms = []
        heapq.heappush(zooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= zooms[0]:
                heapq.heappop(zooms)
            heapq.heappush(zooms, intervals[i][1])
        return len(zooms)
