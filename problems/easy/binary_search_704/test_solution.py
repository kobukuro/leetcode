import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, target, expected, timeout", [
        ('search', [-1, 0, 3, 5, 9, 12], 9, 4, None),
        ('search', [-1, 0, 3, 5, 9, 12], 2, -1, None),
    ])
    def test_search(self, method_name, nums, target, expected, timeout):
        self._run_test(self.solution, method_name, (nums, target,), expected, timeout)
