class Solution:
    def finalString(self, s: str) -> str:
        res = ''
        for c in s:
            if c != 'i':
                res += c
            else:
                res = res[::-1]
        return res
