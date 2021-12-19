# Dynamic Programming
class Solution:
    def combinationSum4(self, nums, target, memo=None):
        if memo is None:
            memo = {}
        if target in memo:
            return memo[target]
        if target == 0:
            return 1
        if target < 0:
            return 0
        total = 0
        for num in nums:
            remainder = target - num
            total += self.combinationSum4(nums=nums, target=remainder, memo=memo)
        memo[target] = total
        return memo[target]


if __name__ == '__main__':
    nums = [9]
    target = 3
    print(Solution().combinationSum4(nums=nums, target=target))
