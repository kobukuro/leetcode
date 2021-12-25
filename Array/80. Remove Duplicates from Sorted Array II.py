# Array
class Solution:
    def removeDuplicates(self, nums):
        a = 0
        b = 0
        hash_map = {}
        while a < len(nums):
            if nums[a] not in hash_map:
                hash_map[nums[a]] = 1
                nums[b] = nums[a]
                b += 1
            elif hash_map[nums[a]] == 1:
                hash_map[nums[a]] += 1
                nums[b] = nums[a]
                b += 1
            a += 1
        return b


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(Solution().removeDuplicates(nums=nums))
    print(nums)
