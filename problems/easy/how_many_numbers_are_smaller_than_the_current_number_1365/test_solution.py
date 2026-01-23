import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, expected, timeout", [
        ('smaller_numbers_than_current', [8, 1, 2, 2, 3], [4, 0, 1, 1, 3], None),
        ('smaller_numbers_than_current', [6, 5, 4, 8], [2, 1, 0, 3], None),
        ('smaller_numbers_than_current', [7, 7, 7, 7], [0, 0, 0, 0], None),
    ])
    def test_smaller_numbers_than_current(self, method_name, nums, expected, timeout):
        self._run_test(self.solution, method_name, (nums,), expected, timeout)
