from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for d in digits:
            s += str(d)
        res_str = str(int(s) + 1)
        res = []
        for c in res_str:
            res.append(int(c))
        return res
