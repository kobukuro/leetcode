# Array
class Solution:
    def removeDuplicates(self, nums):
        a = 0
        b = 0
        seen = set()
        while a < len(nums):
            if nums[a] not in seen:
                seen.add(nums[a])
                nums[b] = nums[a]
                b += 1
            a += 1
        return b


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums=nums))
    print(nums)
