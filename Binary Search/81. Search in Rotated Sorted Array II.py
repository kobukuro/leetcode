# Array, Binary Search
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return True
            elif target < nums[pivot]:
                right = pivot - 1
            elif target > nums[pivot]:
                left = pivot + 1
        return False
