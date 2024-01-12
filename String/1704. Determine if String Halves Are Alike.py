# String, Counting
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        hash_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        a_count = 0
        b_count = 0
        for i in range(len(s) // 2):
            if s[i] in hash_set:
                a_count += 1
        for i in range(len(s) // 2, len(s)):
            if s[i] in hash_set:
                b_count += 1
        return a_count == b_count
