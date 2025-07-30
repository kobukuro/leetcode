import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, intervals, expected, timeout", [
        ('merge', [[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]], None),
        ('merge', [[1,4],[4,5]], [[1,5]], None),
    ])
    def test_merge(self, method_name, intervals, expected, timeout):
        self._run_test(self.solution, method_name, (intervals,), expected, timeout)
