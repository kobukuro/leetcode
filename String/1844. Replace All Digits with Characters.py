# String
class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        for cha in s:
            if cha.isdigit():
                res += chr(ord(res[-1]) + int(cha))
            else:
                res += cha
        return res
