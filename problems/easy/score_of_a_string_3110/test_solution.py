import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('score_of_string', "hello", 13, None),
        ('score_of_string', "zaz", 50, None),
    ])
    def test_score_of_string(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
