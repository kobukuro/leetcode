# Array, Hash Table, Sorting, Counting
from collections import defaultdict


class Solution:
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums
        i = 0
        j = len(nums) - 1
        count = defaultdict(int)
        ans = []
        while i <= j:
            if i != j:
                count[nums[i]] += 1
                count[nums[j]] += 1
                if count[nums[i]] > len(nums) / 3 and nums[i] not in ans:
                    ans.append(nums[i])
                if count[nums[j]] > len(nums) / 3 and nums[j] not in ans:
                    ans.append(nums[j])
            else:
                count[nums[i]] += 1
                if count[nums[i]] > len(nums) / 3 and nums[i] not in ans:
                    ans.append(nums[i])
            i += 1
            j -= 1
        return ans


if __name__ == '__main__':
    nums = [3, 3, 4]
    print(Solution().majorityElement(nums=nums))
