import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('check_string', "aaabbb", True, None),
        ('check_string', "abab", False, None),
        ('check_string', "bbb", True, None),
    ])
    def test_check_string(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
