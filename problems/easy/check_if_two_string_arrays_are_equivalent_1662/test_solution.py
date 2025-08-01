import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, word1, word2, expected, timeout", [
        ('array_strings_are_equal', ["ab", "c"], ["a", "bc"], True, None),
        ('array_strings_are_equal', ["a", "cb"], ["ab", "c"], False, None),
        ('array_strings_are_equal', ["abc", "d", "defg"], ["abcddefg"], True, None),
    ])
    def test_array_strings_are_equal(self, method_name, word1, word2, expected, timeout):
        self._run_test(self.solution, method_name, (word1, word2,), expected, timeout)
