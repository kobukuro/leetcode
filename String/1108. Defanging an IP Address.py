# String
class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        for ele in address:
            if ele == '.':
                res += '[.]'
            else:
                res += ele
        return res
