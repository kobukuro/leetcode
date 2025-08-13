import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, accounts, expected, timeout", [
        ('maximum_wealth', [[1, 2, 3], [3, 2, 1]], 6, None),
        ('maximum_wealth', [[1, 5], [7, 3], [3, 5]], 10, None),
        ('maximum_wealth', [[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17, None),
    ])
    def test_maximum_wealth(self, method_name, accounts, expected, timeout):
        self._run_test(self.solution, method_name, (accounts,), expected, timeout)
