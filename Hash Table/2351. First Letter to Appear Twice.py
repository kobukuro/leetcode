class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_set = set()
        for c in s:
            if c not in hash_set:
                hash_set.add(c)
            else:
                return c
