# Tags: String


class Solution:
    def truncate_sentence(self, s: str, k: int) -> str:
        """
        Time complexity: O(n)
        Breakdown:
        - s.split(): Splits the string into a list of words - O(n) where n is the length of the string
        - [:k]: Slices the first k elements from the list - O(k) where k is the number of words to keep
        - ' '.join(): Joins k words back into a string - O(n) to construct the result string
        Since k <= n (the number of words cannot exceed the string length), overall time complexity is O(n)

        Space complexity: O(n)
        Breakdown:
        - The split() operation creates a list of all words in the string - O(n) space
        - The join() operation creates a new string for the result - O(n) space
        Overall: O(n) additional space
        """
        return ' '.join(s.split()[:k])
