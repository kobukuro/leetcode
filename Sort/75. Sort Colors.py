from typing import List


class QuickSortSolution:
    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    def qs(self, nums, left, right):
        if left >= right:
            return
        index = self.partition(nums, left, right)
        self.qs(nums, left, index - 1)
        self.qs(nums, index + 1, right)

    def quick_sort(self, nums):
        self.qs(nums, 0, len(nums) - 1)

    def sortColors(self, nums: List[int]) -> None:
        self.quick_sort(nums)
