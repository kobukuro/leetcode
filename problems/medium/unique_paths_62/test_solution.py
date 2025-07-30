import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, m, n, expected, timeout", [
        ('unique_paths_memoization', 3, 7, 28, None),
        ('unique_paths_memoization', 3, 2, 3, None),
        ('unique_paths_memoization', 23, 12, 193536720, BaseTestSolution.DEFAULT_TIMEOUT),
        ('unique_paths_tabulation', 3, 7, 28, None),
        ('unique_paths_tabulation', 3, 2, 3, None),
        ('unique_paths_tabulation', 23, 12, 193536720, BaseTestSolution.DEFAULT_TIMEOUT),
    ])
    def test_unique_paths(self, method_name, m, n, expected, timeout):
        self._run_test(self.solution, method_name, (m, n,), expected, timeout)
