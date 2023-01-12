# String, Sliding Window, Hash Table
from collections import defaultdict


# Let n be the number of characters in the string and m be the number of unique characters.
# Time complexity:O(nm).
# We iterate over each unique character once, which requires O(m) time.
# We move a sliding window for each unique character from left to right of the string.
# As the window moves, each character of the string is visited at most two times.
# Once when it enters the window and again when it leaves the window. This adds
# O(n) time complexity for each iteration. So the final time complexity is
# O(nm). For all uppercase English letters, the maximum value of m would be 26.

# Space complexity:O(m).
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_hm = defaultdict(int)
        left = 0
        res = 0
        for right in range(len(s)):
            count_hm[s[right]] += 1
            while (right - left + 1) - max(count_hm.values()) > k:
                count_hm[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
