from collections import defaultdict
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count = defaultdict(int)
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        set_nums3 = set(nums3)
        for num in set_nums1:
            count[num] += 1
        for num in set_nums2:
            count[num] += 1
        for num in set_nums3:
            count[num] += 1
        res = []
        for key, value in count.items():
            if value >= 2:
                res.append(key)
        return res
