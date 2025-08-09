# Tags: String, Two Pointers
from typing import List


class Solution:
    # Time complexity: O(N) to swap N/2 elements.
    # Space complexity: O(1), it's a constant space solution.
    def reverse_string(self, s: List[str]) -> None:
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
