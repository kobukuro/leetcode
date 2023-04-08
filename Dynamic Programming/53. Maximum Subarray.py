# Array, Divide and Conquer, Dynamic Programming
from typing import List


# Time:O(n), Space:O(1)
class Solution:
    def maxSubArray(self, nums):
        res = curr_sum = nums[0]
        for i in range(1, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            res = max(res, curr_sum)
        return res


# Time:O(n), Space:O(n)
class DPSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        return max(dp)


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums=nums))
