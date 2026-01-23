# Tags: Array
from typing import List


class Solution:
    def smaller_numbers_than_current(self, nums: List[int]) -> List[int]:
        """
        For each number in the array, count how many numbers are smaller than it.

        Time Complexity: O(n^2) where n is the length of nums array.
        We use nested loops - for each element (outer loop), we compare it with
        all other elements (inner loop), resulting in quadratic time.

        Space Complexity: O(n) for the result array that stores the count for
        each element. If we don't count the output array, the extra space is O(1).
        """
        res = [0] * len(nums)
        for i in range(len(nums)):
            val = 0
            for j in range(len(nums)):
                if i != j and nums[j] < nums[i]:
                    val += 1
            res[i] = val
        return res
