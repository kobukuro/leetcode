class Solution:
    def checkString(self, s: str) -> bool:
        b_appear = False
        for c in s:
            if c == 'b':
                b_appear = True
            else:
                if b_appear:
                    return False
        return True
