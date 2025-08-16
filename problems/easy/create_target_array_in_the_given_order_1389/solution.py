# Tags: Array
from typing import List


class Solution:
    # Time complexity: O(n²)
    # Analysis:
    # The outer loop runs n times, where n is the length of the input arrays
    # Inside the loop, res.insert(index[i], nums[i]) is called
    # The insert() operation on a Python list has O(n) time complexity in the worst case, because:
    # When inserting at position k,
    # all elements from position k to the end need to be shifted one position to the right
    # In the worst case (inserting at the beginning), this requires shifting all existing elements
    # Since we perform n insertions, and each insertion can take up to O(n) time, the overall time complexity is O(n²)

    # Space Complexity: O(n)
    # Analysis:
    # The algorithm creates a result list res that will eventually contain all n elements from the input
    # No additional data structures that grow with input size are used
    # The space used is proportional to the input size, so the space complexity is O(n)
    # Note: This doesn't count the input arrays nums and index as they are given, only the extra space used by the algorithm
    def create_target_array(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(index)):
            res.insert(index[i], nums[i])
        return res
