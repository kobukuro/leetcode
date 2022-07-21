from typing import List


# Time complexity : O(n^2).
# For every element in the array, say i,
# we are looking at the next nums[i] elements to its right
# aiming to find a index whose value is True in memo hash map.
# nums[i] can be at most n, where n is the length of array nums.
#
# Space complexity : O(2n) = O(n).
# First n originates from recursion.
# Second n comes from the usage of the memo table.
class MemoizationSolution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1

        def dfs(curr_index, nums, memo=None):
            if memo is None:
                memo = {}
            if curr_index in memo:
                return memo[curr_index]
            if curr_index == last_index:
                return True
            furthest_jump = min(nums[curr_index],
                                last_index - curr_index)
            for i in range(1, furthest_jump + 1):
                res = dfs(curr_index + i, nums, memo)
                if res:
                    memo[curr_index] = True
                    return True
            memo[curr_index] = False
            return False

        return dfs(0, nums)


# Time complexity : O(n^2).
# For every element in the array, say i,
# we are looking at the next nums[i] elements to its right
# aiming to find a index whose value is True in dp list.
# nums[i] can be at most n, where n is the length of array nums.
#
# Space complexity : O(n). This comes from the usage of the memo table.
class TabulationSolution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        # print(dp)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            furthest_jump = min(nums[i],
                                len(nums) - 1 - i)
            for j in range(1, furthest_jump + 1):
                if dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]


# Time complexity : O(n). We are doing a single pass through the nums array,
# hence n steps, where n is the length of array nums.
# Space complexity : O(1). We are not using any extra memory.
class GreedySolution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
