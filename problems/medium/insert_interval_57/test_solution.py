import pytest
from .solution import Solution
from tests.base_test import BaseTestSolution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, intervals, new_interval, expected, timeout", [
        ('insert', [[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]], BaseTestSolution.DEFAULT_TIMEOUT),
        ('insert', [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]],
         BaseTestSolution.DEFAULT_TIMEOUT),
    ])
    def test_insert(self, method_name, intervals, new_interval, expected, timeout):
        self._run_test(self.solution, method_name, (intervals, new_interval,), expected, timeout)
