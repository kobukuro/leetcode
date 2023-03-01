# Sliding Window, Hash Table, String
# Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by l and r,
# Space:O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            res = max(res, r - l + 1)
        return res
