import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, arr, expected, timeout", [
        ('unique_occurrences', [1, 2, 2, 1, 1, 3], True, BaseTestSolution.DEFAULT_TIMEOUT),
        ('unique_occurrences', [1, 2], False, BaseTestSolution.DEFAULT_TIMEOUT),
        ('unique_occurrences', [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True, BaseTestSolution.DEFAULT_TIMEOUT),
    ])
    def test_unique_occurrences(self, method_name, arr, expected, timeout):
        self._run_test(self.solution, method_name, (arr,), expected, timeout)
