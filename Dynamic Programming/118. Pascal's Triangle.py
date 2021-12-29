# Dynamic Programming
class Solution:
    def generate(self, numRows):
        def helper(num, index, memo=None):
            if memo is None:
                memo = {}
            key = f'{num} {index}'
            if key in memo:
                return memo[key]
            if index == 0 or index == num - 1:
                return 1
            memo[key] = helper(num=num - 1, index=index - 1, memo=memo) + helper(num=num - 1, index=index,
                                                                                 memo=memo)
            return memo[key]

        ans = []
        for i in range(1, numRows + 1):
            item = []
            for j in range(i):
                item.append(helper(num=i, index=j))
            ans.append(item)
        return ans


if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows=numRows))
