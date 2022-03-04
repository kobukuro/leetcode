# Array, Dynamic Programming
# reference:https://www.youtube.com/watch?v=9rr7csNhRJc
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size
        res = 0
        for i in range(2, size):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = 1 + dp[i - 1]
            res += dp[i]
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().numberOfArithmeticSlices(nums=nums))
