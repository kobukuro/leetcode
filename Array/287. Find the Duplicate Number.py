# Array, Two Pointers, Binary Search, Bit Manipulation
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i == 0:
                pass
            else:
                if nums[i] == prev:
                    return nums[i]
            prev = nums[i]
