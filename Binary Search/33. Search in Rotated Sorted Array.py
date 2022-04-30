# Array, Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                elif nums[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot - 1
            return -1

        def find_rotation_index(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot
                if nums[pivot] >= nums[left]:
                    left = pivot + 1
                else:
                    right = pivot - 1

        if nums[-1] >= nums[0]:
            return binary_search(nums, target)
        rotation_index = find_rotation_index(nums, target)
        # print(rotation_index)
        if target == nums[rotation_index]:
            return rotation_index
        if target >= nums[0]:
            return binary_search(nums[:rotation_index + 1], target)
        else:
            index = binary_search(nums[rotation_index + 1:], target)
            if index == -1:
                return -1
            else:
                return rotation_index + 1 + index
