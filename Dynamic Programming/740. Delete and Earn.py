# Array, Hash Table, Dynamic Programming
# reference:https://www.youtube.com/watch?v=7FCemBxvGw0
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        list_values = sorted(set(nums))
        dp = [0] * len(list_values)
        for i in range(len(dp)):
            if i == 0:
                dp[i] = list_values[i] * count[list_values[i]]
            elif i == 1:
                if list_values[i - 1] == list_values[i] - 1:
                    dp[i] = max(dp[i - 1], list_values[i] * count[list_values[i]])
                else:
                    dp[i] = dp[i - 1] + list_values[i] * count[list_values[i]]
            else:
                if list_values[i - 1] == list_values[i] - 1:
                    dp[i] = max(list_values[i] * count[list_values[i]] + dp[i-2],
                                dp[i-1])
                else:
                    dp[i] = max(list_values[i] * count[list_values[i]] + dp[i - 1],
                                list_values[i] * count[list_values[i]] + dp[i - 2])
        return dp[-1]


if __name__ == '__main__':
    nums = [3, 4, 2]
    print(Solution().deleteAndEarn(nums=nums))  # 6
    nums = [2, 2, 3, 3, 3, 4]
    print(Solution().deleteAndEarn(nums=nums))  # 9
    nums = [1, 2, 3, 15, 16, 17, 18]
    print(Solution().deleteAndEarn(nums=nums))  # 38
    nums = [8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4]  # 61
    print(Solution().deleteAndEarn(nums=nums))
    nums = [1, 8, 5, 9, 6, 9, 4, 1, 7, 3, 3, 6, 3, 3, 8, 2, 6, 3, 2, 2, 1, 2, 9, 8, 7, 1, 1, 10, 6, 7, 3, 9, 6, 10, 5,
            4, 10, 1, 6, 7, 4, 7, 4, 1, 9, 5, 1, 5, 7, 5]
    print(Solution().deleteAndEarn(nums=nums))
