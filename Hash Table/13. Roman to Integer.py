# Hash Table, Math, String
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {'I': 1,
                    'IV': 4,
                    'V': 5,
                    'IX': 9,
                    'X': 10,
                    'XL': 40,
                    'L': 50,
                    'XC': 90,
                    'C': 100,
                    'CD': 400,
                    'D': 500,
                    'CM': 900,
                    'M': 1000}
        i = 0
        total = 0
        while i < len(s):
            if i != len(s) - 1:
                if s[i] + s[i + 1] in hash_map:
                    total += hash_map[s[i] + s[i + 1]]
                    i += 2
                else:
                    total += hash_map[s[i]]
                    i += 1
            else:
                total += hash_map[s[i]]
                i += 1
        return total


if __name__ == '__main__':
    # s = "III"
    # s = "LVIII"
    s = "MCMXCIV"
    print(Solution().romanToInt(s=s))
