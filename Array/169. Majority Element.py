# Array, Hash Table, Divide and Conquer, Sorting, Counting
from collections import defaultdict


class Solution:
    def majorityElement(self, nums):
        i = 0
        j = len(nums) - 1
        count = defaultdict(int)
        ans = None
        while ans is None:
            count[nums[i]] += 1
            count[nums[j]] += 1
            if count[nums[i]] > len(nums) / 2:
                ans = nums[i]
            if count[nums[j]] > len(nums) / 2:
                ans = nums[j]
            i += 1
            j -= 1
        return ans


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums=nums))
