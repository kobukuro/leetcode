# Array, Hash Table, Math, Bit Manipulation, Sorting

# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def missingNumber(self, nums):
        actual_xor = 0
        for num in nums:
            actual_xor ^= num
        expected_xor = 0
        for i in range(0, len(nums) + 1):
            expected_xor ^= i
        return actual_xor ^ expected_xor


# Time complexity : O(n)
# Because the set allows for O(1) containment queries, the main loop runs in O(n) time.
# Creating num_set costs O(n) time, as each set insertion runs in amortized O(1) time,
# so the overall runtime is O(n+n)=O(n).

# Space complexity : O(n)
# nums contains n−1 distinct elements,
# so it costs O(n) space to store a set containing all of them.
class HashSetSolution:
    def missingNumber(self, nums):
        hash_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in hash_set:
                return i
