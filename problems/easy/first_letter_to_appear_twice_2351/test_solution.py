import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('repeated_character', "abccbaacz", "c", BaseTestSolution.DEFAULT_TIMEOUT),
        ('repeated_character', "abcdd", "d", BaseTestSolution.DEFAULT_TIMEOUT),
    ])
    def test_repeated_character(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
