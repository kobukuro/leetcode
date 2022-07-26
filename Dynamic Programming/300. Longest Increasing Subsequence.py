# Dynamic Programming, Array, Binary Search
from typing import List


# Given N as the length of nums,
# Time complexity: O(N^2)
# Because we use two nested for loops.

# Space complexity: O(N)
# The only extra space we use relative to input size is the dp array, which is the same length as nums.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
