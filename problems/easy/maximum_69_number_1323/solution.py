# Tags: Math, Greedy


class Solution:
    def maximum69_number(self, num_char_list: int) -> int:
        """
            Let L be the maximum number of digits nums can have (L=4 in this problem).

            Time complexity: O(L)
            Since the input number num has up to most L digits,
            it requires O(L) time to convert it to an equivalent object and vice versa.
            To sum up, the time complexity is O(L).

            Space complexity: O(L)
            We create an object of length L.
        """
        num_char_list = list(str(num_char_list))
        for i in range(len(num_char_list)):
            if num_char_list[i] == '6':
                num_char_list[i] = '9'
                break
        return int(''.join(num_char_list))
