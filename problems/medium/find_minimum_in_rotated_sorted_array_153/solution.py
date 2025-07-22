# Tags: Array, Binary Search
from typing import List


class Solution:
    # Time complexity:O(log n)
    # Space complexity:O(1)
    def find_min(self, nums: List[int]) -> int | None:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[left]:
            return nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return None
