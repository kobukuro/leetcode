# Tags: Array, Two Pointers
from typing import List


class Solution:
    """
    Remove Duplicates from Sorted Array

    Problem:
        Given a sorted array nums, remove the duplicates in-place such that each
        element appears only once. Return the number of unique elements.

    Approach:
        Since the array is sorted, duplicate elements are always adjacent.
        We can use two pointers:
        - read pointer: scans through the array
        - write pointer: tracks where to place the next unique element

    Complexity:
        Time: O(n) - single pass through the array
        Space: O(1) - in-place modification with no extra data structures
    """

    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place.

        Args:
            nums: A sorted list of integers (may contain duplicates)

        Returns:
            int: The number of unique elements (k). The first k elements
                 of nums will contain the unique elements in sorted order.

        Example:
            Input:  nums = [1,1,2]
            Output: k = 2, nums = [1,2,_]
        """
        # Edge case: empty array
        if not nums:
            return 0

        # Initialize write pointer to 1 (second position)
        # The first element is always unique in a non-empty sorted array
        write = 1

        # Start read pointer from index 1 (compare with previous element)
        for read in range(1, len(nums)):
            # Since array is sorted, duplicates are always adjacent
            # If current element is different from previous, it's a new unique element
            if nums[read] != nums[read - 1]:
                # Copy the unique element to the write position
                nums[write] = nums[read]
                # Move write pointer forward for the next unique element
                write += 1

        # Return the count of unique elements
        return write
