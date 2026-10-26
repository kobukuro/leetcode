# Tags: Array, Hash Table

from collections import Counter


class Solution:
    def unique_occurrences(self, arr: list[int]) -> bool:
        """
        Check whether every distinct value in arr has a unique number of occurrences.

        Args:
            arr: Input list of integers.

        Returns:
            True if no two distinct values occur the same number of times,
            otherwise False.

        Time complexity: O(n)
        - n is the length of arr, k is the number of distinct values (k <= n)
        - Counter(arr) scans the list once and each insertion/update is O(1)
          on average: O(n)
        - count.values() iterates over k counts: O(k)
        - set(...) hashes each of the k counts: O(k)
        - len(...) and the comparison are O(1)
        - Total: O(n) + O(k) + O(k) = O(n), since k <= n
        - Worst case: hash collisions could degrade dict/set operations, but
          this is not a practical concern for small integers
        - Tighter bound: the counts sum to n, so there are at most O(sqrt(n))
          distinct counts if they are all unique; this does not change the
          overall O(n) cost dominated by counting

        Space complexity: O(k)
        - Counter stores one entry per distinct value: O(k)
        - The set of counts holds at most k values (usually far fewer): O(k)
        - No recursion, so no call stack overhead
        - Total auxiliary space: O(k), which is O(n) in the worst case when
          all values are distinct; the output is a single bool: O(1)
        """
        count = Counter(arr)
        return len(set(count.values())) == len(count.keys())
