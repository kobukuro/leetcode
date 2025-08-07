# Tags: Array, Binary Search
from typing import List


class Solution:
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        def find_rotation_index():
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                if nums[mid] < nums[mid - 1]:
                    return mid
                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if nums[-1] > nums[0]:
            return binary_search(0, len(nums) - 1)
        rotation_index = find_rotation_index()
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            return binary_search(0, rotation_index - 1)
        else:
            return binary_search(rotation_index, len(nums) - 1)
