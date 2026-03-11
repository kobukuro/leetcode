import pytest
from .solution import Solution
from tests.base_test import BaseTestSolution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, secret, guess, expected, timeout", [
        ('get_hint', "1807", "7810", "1A3B", BaseTestSolution.DEFAULT_TIMEOUT),
        ('get_hint', "1123", "0111", "1A1B", BaseTestSolution.DEFAULT_TIMEOUT),
    ])
    def test_get_hint(self, method_name, secret, guess, expected, timeout):
        self._run_test(self.solution, method_name, (secret, guess,), expected, timeout)
