# Array, Hash Table, Union Find
from typing import List


# Time complexity : O(n)
# Although the time complexity appears to be quadratic due to the while loop nested within the for loop,
# closer inspection reveals it to be linear.
# Because the while loop is reached only when curr_num marks the beginning of a sequence
# (i.e. curr_num-1 is not present in nums),
# the while loop can only run for n iterations throughout the entire runtime of the algorithm.
# This means that despite looking like O(n⋅n) complexity,
# the nested loops actually run in O(n + n) = O(n) time.
# All other computations occur in constant time, so the overall runtime is linear.

# Space complexity : O(n)
# In order to set up O(1) containment lookups,
# we allocate linear space for a hash table to store the O(n) numbers in nums.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in hash_set:
                curr_num = num
                curr_len = 1
                while curr_num + 1 in hash_set:
                    curr_num = curr_num + 1
                    curr_len += 1
                res = max(res, curr_len)
        return res
