# Tags: String, Sorting


class Solution:
    # Time complexity: O(n log n).
    # Assume that n is the length of s, sorting costs O(n log n)
    # and comparing two strings costs O(n).
    # Sorting time dominates and the overall time complexity is O(n log n).

    # Space complexity: O(1).
    # Space depends on the sorting implementation which,
    # usually, costs O(1) auxiliary space if heapsort is used.
    def is_anagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
