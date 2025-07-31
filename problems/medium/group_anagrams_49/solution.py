# Tags: String, Hash Table, Sorting
from typing import List
from collections import defaultdict


class Solution:
    # Time complexity: O(NKlogK), where N is the length of strs,
    # and K is the maximum length of a string in strs.
    # The outer loop has complexity O(N) as we iterate through each string.
    # Then, we sort each string in O(KlogK) time.

    # Space complexity: O(NK), the total information content stored in ans.
    # It's O(NK) because every word inside the input array, are arrays of characters.
    # At the end of the algorithm, we return Lists of size N,
    # where each element of those lists are arrays of characters - hence O(NK).
    # That's different from a list of Integers - each Integer have a specific number of storage units,
    # and that's why a list of Integers are O(N) space. At the end,
    # it does not matter if the Integer in the list is 1 or 2147483647,
    # they all represent the same storage unit(32 bits).
    # But in a list of arrays of chars,
    # every array of char inside that list occupies storage based on the size of the word.
    # It's not fixed. Every char in a word in that list occupies 2 bytes.
    def group_anagrams_sorted_string(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

    # Time complexity: O(NK), where N is the length of strs,
    # and K is the maximum length of a string in strs.
    # Counting each string is linear in the size of the string, and we count every string.

    # Space complexity: O(NK), the total information content stored in ans.
    def group_anagrams_count(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
