# Tags: Array, String
from typing import List


class Solution:
    def count_matches(self, items: List[List[str]], rule_key: str, rule_value: str) -> int:
        """
        Count the number of items that match the given rule.

        Args:
            items: List of items where each item is [type, color, name]
            rule_key: The key to match against ('type', 'color', or 'name')
            rule_value: The value to match

        Returns:
            Number of items matching the rule

        Time complexity: O(n) where n is the number of items
        - Single loop through all items: O(n)
        - Each iteration does constant time comparisons: O(1)

        Space complexity: O(1)
        - Only uses a single counter variable (res)
        """
        res = 0
        for item in items:
            if rule_key == 'type' and item[0] == rule_value:
                res += 1
            elif rule_key == 'color' and item[1] == rule_value:
                res += 1
            elif rule_key == 'name' and item[2] == rule_value:
                res += 1
        return res
