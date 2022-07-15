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


# Time Complexity: O(N) since we have a loop from 0...len(nums)-1
# and we simply use the pre-calculated values of our dynamic programming table
# for calculating the current value in the table which is a constant time operation.
# Space Complexity: O(N) which is used by the table.
# So what is the real advantage of this solution over the previous solution?
# In this case, we don't have a recursion stack.
# When the number of houses is large, a recursion stack can become a serious limitation,
# because the recursion stack size will be huge
# and the compiler will eventually run into stack-overflow problems (no pun intended!).
class TabulationSolution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        # print(dp)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
