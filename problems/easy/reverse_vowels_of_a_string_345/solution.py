# Tags: String, Two Pointers


class Solution:
    # Here, N is the length of the string s.
    # Time complexity: O(N)
    # It might be tempting to say that there are two nested loops and hence the complexity would be O(N²).
    # However, if we observe closely the pointers start and end will only traverse the index once.
    # Each element of the string s will be iterated only once either by the left or right pointer and not both.
    # We swap characters when both pointers point to vowels which are O(1) operation.
    # Hence the total time complexity will be O(N).

    # Space complexity: O(N)
    # The space complexity analysis:
    # lst = list(s) creates a list copy of the input string, requiring O(N) space
    # The variables l, r use O(1) constant space
    # ''.join(lst) creates a new string from the list, requiring O(N) space
    # The is_vowel() function uses O(1) space
    def reverse_vowels(self, s: str) -> str:
        lst = list(s)
        l = 0
        r = len(lst) - 1
        while l < r:
            while l <= r and not self.is_vowel(lst[l]):
                l += 1
            while r > l and not self.is_vowel(lst[r]):
                r -= 1
            if l > r:
                break
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return ''.join(lst)

    def is_vowel(self, c: str) -> bool:
        return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or \
            c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'
