# Tags: String
class Solution:
    # Time complexity: O(n)
    # n represents the total number of characters in the input string title
    # title.split() takes O(n) time to traverse the entire string and create word boundaries
    # The outer loop iterates through each word,
    # and the inner loop processes each character in words longer than 2 characters
    # In total, every character in the original string is processed exactly once across all iterations
    # ' '.join(words) takes O(n) time to reconstruct the final string
    # Overall: O(n) + O(n) + O(n) = O(n)

    # Space complexity: O(n)
    # n represents the total number of characters in the input string title
    # words = title.split() creates a list containing all words,
    # which collectively store all characters from the original string: O(n)
    # For each word longer than 2 characters, a new_word string is created during processing.
    # In the worst case, this could be O(n) for a single very long word
    # The final result returned by ' '.join(words) creates a new string of length n: O(n)
    # Overall space usage: O(n)
    def capitalize_title(self, title: str) -> str:
        words = title.split()
        for i in range(len(words)):
            if len(words[i]) == 1 or len(words[i]) == 2:
                words[i] = words[i].lower()
            else:
                new_word = ''
                for index, char in enumerate(words[i]):
                    if index == 0:
                        new_word += char.upper()
                    else:
                        new_word += char.lower()
                words[i] = new_word
        return ' '.join(words)
