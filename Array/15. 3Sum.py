# Array, Two Pointers, Sorting
# reference:https://www.youtube.com/watch?v=jzZsG8n2R9A
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    print(Solution().threeSum(nums=nums))
