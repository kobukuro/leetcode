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


# At any given window,
# max_freq will only be violated if the start index happens to be pointing at the char with max frequency.
# For example: "AABBA", start = 0, end = 4.
# If we shrink the window by moving the start pointer to the right by 1, max_freq should be 2 instead of 3.
# Keep in mind that the way we validate the window is by comparing windowLength - max_freq with k.
# When the situation described earlier happens,
# notice that the most frequent char is removed from both the max_freq count as well as the windowLength count.
# In other words "the number of chars that need to be replaced" becomes (windowLength - 1) - (max_freq - 1).
# The two -1s cancel out.
class FasterSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        l = 0
        res = 0
        max_freq = 0
        for r in range(len(s)):
            hm[s[r]] += 1
            max_freq = max(max_freq, hm[s[r]])
            while (r - l + 1) - max_freq > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res
