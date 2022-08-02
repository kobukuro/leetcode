# Array, String
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = list(s)
        index = 0
        for i in range(len(s)):
            res[indices[index]] = s[i]
            index += 1
        return ''.join(res)
