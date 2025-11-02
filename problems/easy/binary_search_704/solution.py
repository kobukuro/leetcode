# Tags: Array, Binary Search
from typing import List


class Solution:
    """
        Let n be the size of the input array nums.

        Time complexity: O(log n)
        nums is divided into half each time.
        In the worst-case scenario, we need to cut nums until the range has no element,
        and it takes logarithmic time to reach this break condition.

        Space complexity: O(1)
        During the loop, we only need to record three indexes, left, right, and mid, they take constant space.
    """

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
