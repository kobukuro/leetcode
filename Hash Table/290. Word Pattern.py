# Hash Table, String
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chrs = s.split(' ')
        if len(pattern) != len(chrs):
            return False
        lookup = {}
        for index, c in enumerate(chrs):
            if pattern[index] in lookup and lookup[pattern[index]] != c:
                return False
            if pattern[index] not in lookup:
                for key, value in lookup.items():
                    if value == c:
                        return False
            lookup[pattern[index]] = c
        return True
