from typing import List
from collections import defaultdict


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            if value % 2 != 0:
                return False
        return True
