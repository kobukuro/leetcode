import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('length_of_last_word', "Hello World", 5, None),
        ('length_of_last_word', "   fly me   to   the moon  ", 4, None),
        ('length_of_last_word', "luffy is still joyboy", 6, None),
    ])
    def test_length_of_last_word(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
