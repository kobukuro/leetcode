# Array, Two Pointers, Sorting
# Time Complexity: O(N), where N is the length of the input array.
# Space Complexity: O(N) if you take output into account and O(1) otherwise.
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = [0] * len(nums)
        index = len(nums) - 1
        while l <= r:
            l_sq, r_sq = nums[l] ** 2, nums[r] ** 2
            if l_sq > r_sq:
                res[index] = l_sq
                l += 1
            else:
                res[index] = r_sq
                r -= 1
            index -= 1
        return res


if __name__ == "__main__":
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
