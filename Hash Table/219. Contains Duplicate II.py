from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lookup = {}
        for index, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = [index]
            else:
                for idx in lookup[num]:
                    if abs(index - idx) <= k:
                        return True
                lookup[num].append(index)
        return False
