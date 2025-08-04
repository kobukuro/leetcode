# Tags: Array
from typing import List


class Solution:
    # Time complexity: O(n)
    # The operation nums + nums requires:
    # Iterating through all elements of the first array: O(n)
    # Iterating through all elements of the second array: O(n)
    # Total: O(n + n) = O(2n) = O(n)
    # Where n is the length of the input array nums.

    # Space complexity: O(n)
    # A new array is created to store the result.
    # The new array has twice the length of the original array: 2n
    # Therefore, the space complexity is: O(2n) = O(n)
    def get_concatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
