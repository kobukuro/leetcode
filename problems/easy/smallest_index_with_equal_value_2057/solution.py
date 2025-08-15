# Tags: Array
from typing import List


class Solution:
    # Time complexity: O(n)
    # The algorithm uses a single for loop that iterates through the entire nums list using enumerate()
    # In the worst case scenario,
    # we need to check every element in the list
    # (when no element satisfies the condition idx % 10 == num,
    # or when the satisfying element is at the last position)
    # Each iteration performs a constant time operation: modulo calculation (idx % 10) and comparison (== num)
    # Therefore, the time complexity is O(n), where n is the length of the input list

    # Space complexity: O(1)
    def smallest_equal(self, nums: List[int]) -> int:
        for idx, num in enumerate(nums):
            if idx % 10 == num:
                return idx
        return -1
