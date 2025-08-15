import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, expected, timeout", [
        ('smallest_equal', [0, 1, 2], 0, None),
        ('smallest_equal', [4, 3, 2, 1], 2, None),
        ('smallest_equal', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0], -1, None),
    ])
    def test_smallest_equal(self, method_name, nums, expected, timeout):
        self._run_test(self.solution, method_name, (nums,), expected, timeout)
