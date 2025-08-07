import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, target, expected, timeout", [
        ('search', [4, 5, 6, 7, 0, 1, 2], 0, 4, None),
        ('search', [4, 5, 6, 7, 0, 1, 2], 3, -1, None),
        ('search', [1], 0, -1, None),
    ])
    def test_search(self, method_name, nums, target, expected, timeout):
        self._run_test(self.solution, method_name, (nums, target,), expected, timeout)
