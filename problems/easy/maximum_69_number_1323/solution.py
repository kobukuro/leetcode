# Tags: Math, Greedy


class Solution:
    def maximum69_number(self, num: int) -> int:
        """
            Let L be the number of digits of the input number (L <= 4 in this problem).

            Time complexity: O(L)
            Since the input number has at most L digits,
            it requires O(L) time to convert it to a list of characters, modify it, and convert it back.

            Space complexity: O(L)
            We create a list of characters whose length is L.
        """
        num_char_list = list(str(num))
        for i in range(len(num_char_list)):
            if num_char_list[i] == '6':
                num_char_list[i] = '9'
                break
        return int(''.join(num_char_list))
