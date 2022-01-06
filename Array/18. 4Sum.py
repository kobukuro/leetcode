# Array
class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        ans = []
        nums.sort()
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums) - 1):
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum > target:
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        if [nums[i], nums[j], nums[l], nums[r]] not in ans:
                            ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
        return ans


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 2]
    target = 8
    print(Solution().fourSum(nums=nums, target=target))
