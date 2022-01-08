# Array, Hash Table, Math, Bit Manipulation, Sorting
class Solution:
    def missingNumber(self, nums):
        ans = 0
        for i in range(len(nums) + 1):
            if i not in nums:
                ans = i
        return ans


if __name__ == '__main__':
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums=nums))
