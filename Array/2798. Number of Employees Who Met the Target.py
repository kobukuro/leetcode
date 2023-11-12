from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for hour in hours:
            if hour >= target:
                res += 1
        return res
