# Array, Dynamic Programming

from typing import List


# Time Complexity: O(N) since we process at most N recursive calls,
# thanks to caching, and during each of these calls,
# we make an O(1) computation which is simply making two other recursive calls,
# finding their maximum, and populating the cache based on that.
# Space Complexity: O(N) which is occupied by the cache and also by the recursion stack.
class MemoizationSolution:
    def rob(self, nums: List[int]) -> int:
        last_index = len(nums) - 1

        def dfs(curr_index, nums, memo=None):
            if memo is None:
                memo = {}
            if curr_index in memo:
                return memo[curr_index]
            if curr_index == last_index:
                return nums[-1]
            if curr_index > last_index:
                return 0
            ans = max(nums[curr_index] + dfs(curr_index + 2, nums, memo),
                      dfs(curr_index + 1, nums, memo))
            memo[curr_index] = ans
            return memo[curr_index]

        return dfs(0, nums)
