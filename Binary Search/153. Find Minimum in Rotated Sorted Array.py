# Array, Binary Search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = nums[0]
        while left <= right:
            print(left, right)
            pivot = (left + right) // 2
            print(pivot)
            res = min(res, nums[pivot], nums[left])
            if nums[pivot] >= nums[left]:
                left = pivot + 1
            else:
                right = pivot - 1
        return res
