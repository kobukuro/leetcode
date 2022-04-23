# Array, Hash Table, Sorting
# Time:O(n), Space:O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().containsDuplicate(nums=nums))
