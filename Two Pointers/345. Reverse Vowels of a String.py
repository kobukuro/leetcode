# Two Pointers, String
class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        start = 0
        end = len(lst) - 1
        while start < end:
            while start <= len(lst) - 1 and lst[start] not in vowels:
                start += 1
            while end >= 0 and lst[end] not in vowels:
                end -= 1
            if start >= end:
                break
            lst[start], lst[end] = lst[end], lst[start]
            # print(lst)
            start += 1
            end -= 1
        return ''.join(lst)
