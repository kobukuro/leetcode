import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, expected, timeout", [
        ('rob_memoization', [1, 2, 3, 1], 4, None),
        ('rob_memoization', [2, 7, 9, 3, 1], 12, None),
        ('rob_tabulation', [1, 2, 3, 1], 4, None),
        ('rob_tabulation', [2, 7, 9, 3, 1], 12, None),
    ])
    def test_rob(self, method_name, nums, expected, timeout):
        self._run_test(self.solution, method_name, (nums,), expected, timeout)
