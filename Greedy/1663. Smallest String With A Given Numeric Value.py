# String, Greedy
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # aaa -> k = 27-3=24
        # aa
        # print(chr(97))
        # print(chr(97+24))
        # print(ord('a'))
        ans = ['a'] * n
        # print(ans)
        k -= n
        for i in range(len(ans) - 1, -1, -1):
            # print(k)
            if k <= 0:
                break
            ans[i] = chr(97 + min(k + 1, 26) - 1)
            k = k + 1 - (ord(ans[i]) - 96)
            # print(k)
        return ''.join(ans)
