# Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum
from typing import List
import heapq


# Time Complexity: O(NlogN).
# There are two major portions that take up time here.
# One is sorting of the array that takes O(NlogN) considering that the array consists of N elements.
# Then we have the min-heap. In any case we have N add operations on the heap.
# Overall complexity being (NlogN) since ADD operation on a heap takes O(logN).
# Space Complexity: O(N) because we construct the min-heap and that can contain N elements
# when N meetings will collide with each other.
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
