# Array
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums) - 1, 2):
            for j in range(nums[i]):
                res.append(nums[i + 1])
        return res
