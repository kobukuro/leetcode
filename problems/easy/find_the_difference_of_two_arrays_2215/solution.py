# Tags: Array, Hash Table
from typing import List


class Solution:
    # Here, N is the length of list nums1, and M is the length of nums2.
    # Time complexity: O(N + M)
    # Breakdown:
    # Converting nums1 to nums1_set: O(N)
    # Converting nums2 to nums2_set: O(M)
    # First list comprehension: O(N) - iterates through nums1_set and performs O(1) hash table lookups
    # Second list comprehension: O(M) - iterates through nums2_set and performs O(1) hash table lookups
    # Total: O(N + M + N + M) = O(N + M)

    # Space complexity: O(N + M)
    # Breakdown:
    # nums1_set: O(N) space to store unique elements from nums1
    # nums2_set: O(M) space to store unique elements from nums2
    # Result lists: In worst case, O(n + m) when there's no overlap between the sets
    # Temporary space for list comprehensions: O(n + m) in worst case
    def find_difference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return [[num for num in nums1_set if num not in nums2_set],
                [num for num in nums2_set if num not in nums1_set]]
