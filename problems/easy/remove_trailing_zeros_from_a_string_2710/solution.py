# Tags: String


class Solution:
    def remove_trailing_zeros(self, num: str) -> str:
        """
        Remove trailing zeros from a string representation of a positive integer.

        Args:
            num: A string representation of a positive integer without leading zeros

        Returns:
            The string representation of the integer without trailing zeros

        Time complexity: O(n) where n is the length of the input string
        - Worst case: O(n) when iterating through the entire string (e.g., "10000", "5")
        - Best case: O(1) when the last character is already non-zero
        - The loop traverses from the end until finding the first non-zero digit

        Space complexity: O(n) for the result string, O(1) auxiliary space
        - O(n) for the result string which is required output
        - O(1) additional space for the 'res' variable and loop counter
        """
        res = ""
        for i in range(len(num) - 1, -1, -1):
            if not res and num[i] != "0":
                res = num[: i + 1]
                break
        return res
