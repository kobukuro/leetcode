# Tags: Array, String, Simulation
from typing import List


class Solution:
    def final_value_after_operations(self, operations: List[str]) -> int:
        """
        Time Complexity: O(n)
            - We iterate through the operations list once, where n is the length of operations
            - Each operation involves constant time string indexing and arithmetic operations

        Space Complexity: O(1)
            - We only use a constant amount of extra space for the result variable
            - No additional data structures are created
        """
        res = 0
        for operation in operations:
            if operation[1] == '+':
                res += 1
            else:
                res -= 1
        return res
