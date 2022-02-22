# Math, String
import math


# slow
# class Solution:
#     # A  -> 1
#     # AA -> 26*1 + 1 = 27
#     # AAA-> 26*26*1 + 26*1 + 1 = 703
#     def titleToNumber(self, columnTitle: str) -> int:
#         result = 0
#         digit_num = 0
#         for i in range(len(columnTitle) - 1, -1, -1):
#             # print(columnTitle[i])
#             result += int(math.pow(26, digit_num)) * (ord(columnTitle[i]) - ord('A') + 1)
#             digit_num += 1
#         return result

# fast
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            d = ord(c) - ord('A') + 1
            result = result * 26 + d
        return result


if __name__ == '__main__':
    print(Solution().titleToNumber(columnTitle='AAA'))
