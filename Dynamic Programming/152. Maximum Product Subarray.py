# Array, Dynamic Programming
# Time:O(n), Space:O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = max_so_far = res = nums[0]
        for i in range(1, len(nums)):
            temp_min_so_far = min(nums[i], min_so_far * nums[i], max_so_far * nums[i])
            max_so_far = max(nums[i], min_so_far * nums[i], max_so_far * nums[i])
            min_so_far = temp_min_so_far
            res = max(res, max_so_far)
            # print(min_so_far, max_so_far, res)
        return res
