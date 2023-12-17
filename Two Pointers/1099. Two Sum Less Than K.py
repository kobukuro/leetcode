# Array, Two Pointers, Binary Search, Sorting
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = -1
        while l < r:
            sum_val = nums[l] + nums[r]
            if sum_val < k:
                res = max(res, sum_val)
            if sum_val >= k:
                r -= 1
            else:
                l += 1
        return res
