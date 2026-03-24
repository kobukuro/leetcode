# Tags: String
class Solution:
    def check_string(self, s: str) -> bool:
        """
        Time Complexity: O(n) where n is the length of string s
                         - We iterate through the string exactly once
        Space Complexity: O(1)
                          - Only a single boolean variable is used
        """
        is_b_appear = False
        for c in s:
            if c == 'b':
                is_b_appear = True
            else:
                if is_b_appear:
                    return False
        return True
