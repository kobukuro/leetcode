from typing import List


class Solution:
    # Time:O(n), We do search() and insert() for n times and each operation takes constant time.
    # Space:O(n), The space used by a hash set is linear with the number of elements in it.
    def contains_duplicate(self, nums: List[int]) -> bool:
        lookup = set()
        for num in nums:
            if num in lookup:
                return True
            lookup.add(num)
        return False
