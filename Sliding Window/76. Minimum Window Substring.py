# Hash Table, String, Sliding Window
from collections import defaultdict


# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        res_len = float('inf')
        need_hm = defaultdict(int)
        for cha in t:
            need_hm[cha] += 1
        need = len(need_hm.keys())
        have_hm = {cha: 0 for cha in t}
        have = 0
        l = 0
        for r in range(len(s)):
            if s[r] in have_hm:
                have_hm[s[r]] += 1
                if have_hm[s[r]] == need_hm[s[r]]:
                    have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                if s[l] in have_hm:
                    have_hm[s[l]] -= 1
                    if have_hm[s[l]] < need_hm[s[l]]:
                        have -= 1
                l += 1
        return s[res[0]:res[1] + 1] if res_len != float('inf') else ''
