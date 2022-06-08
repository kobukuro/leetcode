# Array, Hash Table, String, Sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            if str(sorted(s)) not in hash_map:
                hash_map[str(sorted(s))] = [s]
            else:
                hash_map[str(sorted(s))].append(s)
        return hash_map.values()
