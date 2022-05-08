# Array, Two Pointers, Stack, Greedy, Sorting, Monotonic Stack
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        print(nums)
        print(sorted_nums)
        indices = []
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if len(indices) == 0:
                    indices.append(i)
                elif len(indices) == 1:
                    indices.append(i)
                else:
                    indices[1] = i
        return indices[1] - indices[0] + 1 if indices else 0
