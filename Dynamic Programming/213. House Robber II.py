# Array, Dynamic Programming
from typing import List


# Time Complexity: O(N)
# Space Complexity: O(N)
class MemoizationSolution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(curr_index, nums, memo=None):
            if memo is None:
                memo = {}
            if curr_index in memo:
                return memo[curr_index]
            if curr_index > len(nums) - 1:
                return 0
            res = max(nums[curr_index] + dfs(curr_index + 2, nums, memo),
                      dfs(curr_index + 1, nums, memo))
            memo[curr_index] = res
            return memo[curr_index]

        return max(dfs(0, nums[:-1]), dfs(0, nums[1:]))


# Time Complexity: O(N)
# Space Complexity: O(N)
class TabulationSolution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_dp(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            return dp[-1]

        return max(rob_dp(nums[:-1]), rob_dp(nums[1:]))
