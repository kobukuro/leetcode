# Array, Hash Table, String, Sorting

# Time Complexity: O(NKlogK), where N is the length of strs,
# and K is the maximum length of a string in strs.
# The outer loop has complexity O(N) as we iterate through each string.
# Then, we sort each string in O(KlogK) time.
# Space Complexity: O(NK), the total information content stored in hash_map.
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
class SortingSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [s]
            else:
                hash_map[sorted_str].append(s)
        return hash_map.values()


# Time Complexity: O(NK), where N is the length of strs,
# and K is the maximum length of a string in strs.
# Counting each string is linear in the size of the string, and we count every string.
# Space Complexity: O(NK), the total information content stored in hash_map.
class CountingSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return hash_map.values()
