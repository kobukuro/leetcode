# Tags: String


class Solution:
    # Here, N is the number of characters in the string s.
    # Time complexity: O(N)
    # We need to iterate over each character in the string s once, hence, the total time complexity is equal to O(N).

    # Space complexity: O(1)
    # The space occupied by the return value is generally not counted towards the total space complexity.
    # Therefore, for this problem, the space complexity is only O(1).
    def remove_vowels(self, s: str) -> str:
        res = ''
        for c in s:
            if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u':
                res += c
        return res
