# Tags: Hash Table, String
class Solution:
    def repeated_character(self, s: str) -> str:
        """
        Return the first letter whose second occurrence appears earliest in s.

        Args:
            s: Input string of lowercase English letters in which at least one
                letter appears twice.

        Returns:
            The first letter to appear twice, i.e. the letter whose second
            occurrence has the smallest index.

        Time complexity: O(n)
        - n is the length of s, k is the number of distinct letters (k <= n)
        - The for loop visits each character at most once, so at most n iterations
        - Each iteration does one set membership test (`c in seen`) and at most
          one set insertion (`seen.add(c)`), both O(1) on average
        - Cost per iteration is O(1), so the total is O(n) * O(1) = O(n)
        - Best case: the first repeat is found early (e.g. "aa") and the loop
          returns after 2 iterations: O(1)
        - Worst case: the repeat is at the very end, so the loop runs through
          all n characters: O(n)
        - Hash collisions could degrade set operations to O(k) in theory, but
          with single-character keys this is not a practical concern
        - Under the problem constraints (lowercase letters only), the loop runs
          at most 27 iterations (26 distinct letters + 1 repeat), because by the
          pigeonhole principle the 27th character must repeat an earlier one,
          so the time is effectively O(1)

        Space complexity: O(k)
        - The set `seen` stores each distinct letter at most once: O(k)
        - Because the loop returns on the first repeat, `seen` never holds more
          than min(n, alphabet size) letters
        - No recursion, slicing or copying, so there is no extra call stack or
          temporary storage; the returned single character is O(1)
        - With a fixed alphabet of 26 lowercase letters, k <= 26, so the
          auxiliary space is O(1)
        """
        seen = set()
        for c in s:
            if c in seen:
                return c
            seen.add(c)
