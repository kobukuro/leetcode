# Tags: String
class Solution:
    # Time complexity: O(N), where N is the length of the input string.
    # Since we use some built-in function from the String data type,
    # we should look into the complexity of each built-in function that we used,
    # in order to obtain the overall time complexity of our algorithm.
    # It would be safe to assume the time complexity of the method str.split() to be O(N),
    # since in the worst case we would need to scan the entire string.

    # Space complexity: O(N).
    # Again, we should look into the built-in functions that we used in the algorithm.
    # we used str.split(), which returns a list of substrings that are separated by the space delimiter.
    # As a result, we would need O(N) space for our algorithm to store this list.
    def length_of_last_word(self, s: str) -> int:
        return len(s.split()[-1])
