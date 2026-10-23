import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, grid, expected, timeout", [
        ('maximum_minutes', [[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 1, 0], [0, 2, 0, 0, 1, 2, 0], [0, 0, 2, 2, 2, 0, 2],
                             [0, 0, 0, 0, 0, 0, 0]], 3, BaseTestSolution.DEFAULT_TIMEOUT),
        ('maximum_minutes', [[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]], -1, BaseTestSolution.DEFAULT_TIMEOUT),
        ('maximum_minutes', [[0, 0, 0], [2, 2, 0], [1, 2, 0]], 1000000000, BaseTestSolution.DEFAULT_TIMEOUT),
        # no fire at all
        ('maximum_minutes', [[0, 0], [0, 0]], 1000000000, BaseTestSolution.DEFAULT_TIMEOUT),
        # fire and person reach the safehouse at the same minute, which still counts as safe
        ('maximum_minutes', [[0, 0, 0, 0, 0], [0, 0, 0, 2, 0], [1, 2, 0, 0, 0]], 0, BaseTestSolution.DEFAULT_TIMEOUT),
        # start is walled in, safehouse unreachable even without fire
        ('maximum_minutes', [[0, 2, 0], [2, 0, 0], [0, 0, 0]], -1, BaseTestSolution.DEFAULT_TIMEOUT)])
    def test_maximum_minutes(self, method_name, grid, expected, timeout):
        self._run_test(self.solution, method_name, (grid,), expected, timeout)
