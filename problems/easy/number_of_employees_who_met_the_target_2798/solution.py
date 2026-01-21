# Tags: Array
from typing import List


class Solution:
    def number_of_employees_who_met_target(self, hours: List[int], target: int) -> int:
        """
        Count the number of employees who met or exceeded the target hours.

        Time Complexity: O(n) where n is the length of hours array.
        We iterate through the array once, performing a constant-time comparison for each element.

        Space Complexity: O(1) as we only use a constant amount of extra space
        for the result variable, regardless of input size.
        """
        res = 0
        for hour in hours:
            if hour >= target:
                res += 1
        return res
