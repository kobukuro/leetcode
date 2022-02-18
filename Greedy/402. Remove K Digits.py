# String, Stack, Greedy, Monotonoc Stack
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        res = []
        stack = []
        i = 0
        while i < len(num):
            while k > 0 and stack != [] and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while k > 0:
            stack.pop()
            k -= 1
        while stack:
            res += stack.pop()
        res.reverse()
        # delete leading zeros
        while len(res) > 1:
            if res[0] == '0':
                res.pop(0)
            else:
                break
        return ''.join(res)


if __name__ == '__main__':
    # print(Solution().removeKdigits(num="1432219", k=3))
    # print(Solution().removeKdigits(num="10200", k=1))
    # print(Solution().removeKdigits(num="10", k=2))
    # print(Solution().removeKdigits(num="112", k=1))
    print(Solution().removeKdigits(num="1234567890", k=9))
