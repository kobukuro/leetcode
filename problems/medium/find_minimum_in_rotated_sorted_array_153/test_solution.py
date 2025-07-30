import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, expected, timeout", [
        ('find_min', [3, 4, 5, 1, 2], 1, None),
        ('find_min', [4, 5, 6, 7, 0, 1, 2], 0, None),
        ('find_min', [11, 13, 15, 17], 11, None),
    ])
    def test_find_min(self, method_name, nums, expected, timeout):
        self._run_test(self.solution, method_name, (nums,), expected, timeout)
