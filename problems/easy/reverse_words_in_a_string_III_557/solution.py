# Tags: String
class Solution:
    def reverse_words(self, s: str) -> str:
        """
        Reverse each word in a string while preserving the word order.

        Time Complexity: O(n)
        - s.split(): O(n) to split the string into words
        - Generator expression with word[::-1]: O(n) total to reverse all characters
        - ' '.join(): O(n) to join the reversed words back together
        - Overall: O(n) where n is the length of the input string

        Space Complexity: O(n)
        - s.split() creates a list of words: O(n) characters stored
        - Generator expression produces reversed strings on-the-fly: O(1) auxiliary space
        - Final joined string: O(n) characters
        - Overall: O(n) where n is the length of the input string
        """
        return ' '.join(word[::-1] for word in s.split())
