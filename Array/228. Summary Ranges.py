# Array
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        size = len(nums)
        temp = []
        for i in range(size):
            if not temp:
                temp.append(nums[i])
            else:
                if temp[-1] == nums[i] - 1:
                    if len(temp) == 1:
                        temp.append(nums[i])
                    else:
                        temp[-1] = nums[i]
                else:
                    if len(temp) == 1:
                        res.append(str(temp[0]))
                    elif len(temp) > 1:
                        res.append(f'{temp[0]}->{temp[1]}')
                    temp = [nums[i]]
        if len(temp) == 1:
            res.append(str(temp[0]))
        elif len(temp) > 1:
            res.append(f'{temp[0]}->{temp[1]}')
        return res


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print(Solution().summaryRanges(nums=nums))
