# Array
from typing import List
from collections import defaultdict


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = defaultdict(int)
        threshold = len(arr) // 4
        for num in arr:
            count[num] += 1
            if count[num] > threshold:
                return num
