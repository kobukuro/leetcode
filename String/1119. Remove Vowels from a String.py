# String
class Solution:
    def removeVowels(self, s: str) -> str:
        hash_set = {'a', 'e', 'i', 'o', 'u'}
        res = ''
        for cha in s:
            if cha not in hash_set:
                res += cha
        return res
