# Tags: Array
from typing import List


class Solution:
    # Here, n is the number of kids.
    # Time complexity: O(n)
    # We iterate over the candies array to find out max_candies which takes O(n) time.
    # We iterate over the candies array once more.
    # We check for each kid whether they will have the most candies
    # among all the children after receiving extraCandies
    # and push the result in res which takes O(1) time. It requires O(n) time for n kids.

    # Space complexity: O(1)
    # Without counting the space of input and output,
    # we are not using any space except for the integer max_candies.
    def kids_with_candies(self, candies: List[int], extra_candies: int) -> List[bool]:
        res = []
        max_candies = max(candies)
        for candy in candies:
            res.append(candy + extra_candies >= max_candies)
        return res
