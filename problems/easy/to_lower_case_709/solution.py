# Tags: String


class Solution:
    # Time Complexity: O(n)
    # The s.lower() method has a time complexity of O(n),
    # where n is the length of the input string s. This is because:
    # - The method needs to iterate through each character in the string
    # - For each character, it performs a constant-time operation to convert it to lowercase
    # - Since there are n characters to process, the overall time complexity is O(n)

    # Space Complexity: O(n)
    # The space complexity is O(n) because:
    # - The s.lower() method creates and returns a new string object
    # - In Python, strings are immutable, so any modification operation creates a new string
    # - The new string has the same length as the input string, requiring O(n) additional space
    # - The original string s still exists in memory,
    # so we need space for both the original and the new lowercase string
    def to_lower_case(self, s: str) -> str:
        return s.lower()
