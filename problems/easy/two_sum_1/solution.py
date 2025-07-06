# Tags: Hash Table
class Solution:
    def two_sum(self, nums, target):
        # We use a dictionary here,
        # because for the purpose of an interview, we often just summarize that
        # getting and setting in a hash table is constant time.(O(1))

        # Time complexity: O(n).
        # We traverse the list containing n elements only once.
        # Each lookup in the table costs only O(1) time.
        # Space complexity: O(n).
        # The extra space required depends on the number of items stored in the hash table,
        # which stores at most n elements.
        lookup = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], idx]
            lookup[num] = idx
        return []
