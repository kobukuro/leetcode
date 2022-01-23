# Array, Hash Table, Sorting
# TODO need to be improved
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        i = 0
        while i < len(nums):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = 1
            else:
                return True
            i += 1
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().containsDuplicate(nums=nums))
