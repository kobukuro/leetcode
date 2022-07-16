# Array, Dynamic Programming
from typing import List


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
