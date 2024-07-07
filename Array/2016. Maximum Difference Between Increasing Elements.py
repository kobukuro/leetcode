# Array
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > min_val:
                res = max(res, nums[i] - min_val)
            min_val = min(min_val, nums[i])
        return res
