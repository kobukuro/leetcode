# Tags: Array, Two Pointers
from typing import List


class Solution:
    """
    Time complexity: O(m + n)
    Breakdown:
    -   First while loop: Compares elements from both arrays and places them in the correct position
        -   In each iteration, either p1 or p2 decrements by 1
        -   The loop continues until one of the pointers reaches -1
        -   Maximum iterations: min(m, n)
    -   Second while loop: Copies remaining elements from nums2 (if any)
        -   Runs at most n iterations (when all elements from nums2 need to be copied)
    -   Total operations: Each element from both arrays is processed exactly once
    -   Overall: O(m + n)
    Where m is the number of valid elements in nums1 and n is the number of elements in nums2.

    Space complexity: O(1)
    Breakdown:
    -   In-place modification: The algorithm modifies nums1 directly without using additional arrays
    -   Pointer variables: p1, p2, and index use constant space O(1)
    -   No extra data structures: No additional arrays, lists, or collections are created
    -   Overall: O(1) - constant space complexity
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, index = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[index] = nums1[p1]
                p1 -= 1
            else:
                nums1[index] = nums2[p2]
                p2 -= 1
            index -= 1
        while p2 >= 0:
            nums1[index] = nums2[p2]
            index -= 1
            p2 -= 1
