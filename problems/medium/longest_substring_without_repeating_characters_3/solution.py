# Tags: Sliding Window
class Solution:
    # Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by l and r,
    # Space complexity : O(n)
    def length_of_longest_substring_sliding_window(self, s: str) -> int:
        res = 0
        chars = set()
        l = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res
