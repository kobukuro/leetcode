# Tags: Array, Two Pointers
from typing import List


class Solution:
    # Time complexity: O(N), where N is the length of the input array.
    # Space complexity: O(N) if you take output into account and O(1) otherwise.
    def sorted_squares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        index = len(res) - 1
        while l <= r:
            l_sq, r_sq = nums[l] * nums[l], nums[r] * nums[r]
            if l_sq >= r_sq:
                res[index] = l_sq
                l += 1
            else:
                res[index] = r_sq
                r -= 1
            index -= 1
        return res
