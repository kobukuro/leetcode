import pytest
from .solution import Solution
from tests.base_test import BaseTestSolution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, heights, expected, timeout", [
        ('pacific_atlantic',
         [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
         [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], None),
        ('pacific_atlantic', [[1]], [[0, 0]], None),
    ])
    def test_pacific_atlantic(self, method_name, heights, expected, timeout):
        self._run_test(self.solution, method_name, (heights,), expected, timeout)
