# Array, Sorting
from typing import List


# Time complexity : O(nlogn).
# The time complexity is dominated by sorting.
# Once the array has been sorted,
# only O(n) time is taken to go through the array and determine if there is any overlap.
# Space complexity : O(1). Since no additional space is allocated.
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
