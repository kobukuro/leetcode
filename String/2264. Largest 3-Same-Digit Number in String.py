class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ''
        start = 0
        while start + 2 < len(num):
            lookup = set()
            for c in num[start:start + 3]:
                lookup.add(c)
            if len(lookup) == 1:
                if not res:
                    res = num[start:start + 3]
                elif int(num[start:start + 3]) > int(res):
                    res = num[start:start + 3]
            start += 1
        return res
