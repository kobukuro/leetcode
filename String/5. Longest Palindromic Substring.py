# String, Dynamic Programming
# Time complexity : O(n^2)
# Since expanding a palindrome around its center could take O(n) time,
# the overall complexity is O(n^2).

# Space complexity : O(1).
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1
        return res
