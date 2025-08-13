# Tags: Array, Matrix
from typing import List


class Solution:
    # Let M be the number of customers and N be the number of banks.
    # Time complexity: O(M⋅N)
    # For each of the M customers,
    # we need to iterate over all N banks to find the sum of his/her wealth.
    # Hence, the total time complexity is O(M⋅N).

    # Space complexity: O(1)
    # We only need two variables max_wealth_so_far and curr_customer_wealth
    # to store the wealth of the current customer,
    # and the highest wealth we have seen so far respectively.
    # Therefore, the space complexity is constant.
    def maximum_wealth(self, accounts: List[List[int]]) -> int:
        max_wealth_so_far = 0

        for account in accounts:
            curr_customer_wealth = sum(account)
            max_wealth_so_far = max(max_wealth_so_far, curr_customer_wealth)

        return max_wealth_so_far
