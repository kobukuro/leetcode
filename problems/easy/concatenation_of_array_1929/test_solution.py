import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, expected, timeout", [
        ('get_concatenation', [1, 2, 1], [1, 2, 1, 1, 2, 1], None),
        ('get_concatenation', [1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1], None),
    ])
    def test_get_concatenation(self, method_name, nums, expected, timeout):
        self._run_test(self.solution, method_name, (nums,), expected, timeout)
