# Time complexity : O(n), in length n of the string.
# We need to iterate thrice through the string:
# When we filter out non-alphanumeric characters, and convert the remaining characters to lower-case.
# When we reverse the string.
# When we compare the original and the reversed strings.
# Each iteration runs linear in time
# (since each character operation completes in constant time).
# Thus, the effective run-time complexity is linear.
# Space complexity : O(n), in length n of the string.
# We need O(n) additional space to stored the filtered string and the reversed string.
class FirstSolution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for cha in s:
            if cha.isalnum():
                new_str += cha.lower()
        return new_str == new_str[::-1]


# Time complexity : O(n), in length n of the string.
# We traverse over each character at-most once,
# until the two pointers meet in the middle, or when we break and return early.
# Space complexity : O(1). No extra space required, at all.
class TwoPointerSolution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
