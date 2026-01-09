# Tags: Array, Hash Set
from typing import List


class Solution:
    def get_sneaky_numbers(self, nums: List[int]) -> List[int]:
        """
            Find two numbers that appear twice in the array.

            Time Complexity: O(n)
                - We iterate through the array once, where n is the length of nums
                - Each lookup and insertion in the hash set takes O(1) on average
                - In the worst case, we visit all elements before finding both duplicates
                - Overall: O(n)

            Space Complexity: O(n)
                - In the worst case, we store all unique elements in the 'seen' set
                - The 'res' list stores at most 2 elements, which is O(1)
                - Overall: O(n) for the hash set
        """
        res = []
        seen = set()
        for num in nums:
            if num in seen:
                res.append(num)
                if len(res) == 2:
                    return res
            else:
                seen.add(num)
        return res
