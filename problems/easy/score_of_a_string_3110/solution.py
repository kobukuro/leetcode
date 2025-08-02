# Tags: String


class Solution:
    # Here, n is the length of the input string.
    # Time complexity: O(n)
    # The process involves iterating through the string once,
    # from the first character to the second-last character, making it a linear iteration over n-1 indices
    # At each index, calculating the absolute difference
    # between the ASCII values of two adjacent characters requires constant time.
    # Hence, the total time complexity for this operation is O(n-1)=O(n).

    # Space Complexity: O(1)
    # We only used a single additional variable, score, to accumulate the result.
    # Therefore, the space complexity is O(1),
    # indicating that no additional space proportional to the input size is required.
    def score_of_string(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
