# Math, String
# 背起來
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            d = ord(c) - ord('A') + 1
            result = result * 26 + d
        return result


if __name__ == '__main__':
    print(Solution().titleToNumber(columnTitle='BA'))
