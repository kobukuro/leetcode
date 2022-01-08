# Array, Divide and Conquer, Dynamic Programming
# reference:https://www.youtube.com/watch?v=5WZl3MMT0Eg
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        curr_sum = 0
        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums=nums))
