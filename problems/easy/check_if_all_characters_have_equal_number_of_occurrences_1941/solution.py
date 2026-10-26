# Tags: String, Hash Table
from collections import Counter


class Solution:
    def are_occurrences_equal(self, s: str) -> bool:
        """
        Time complexity: O(n)
        - n represents the length of the input string s
        - Counter(s) traverses the entire string once: O(n)
        - count_table.values() extracts frequency values: O(k), k = unique chars
        - set() removes duplicates: O(k)
        - len() calculates set size: O(1)
        - Since k <= n, overall: O(n)

        Space complexity: O(k)
        - k represents the number of unique characters
        - Counter stores k character-frequency pairs: O(k)
        - The set of unique frequencies: O(k)
        - Overall: O(k), where k <= n
        """
        count_table = Counter(s)
        return len(set(count_table.values())) == 1
