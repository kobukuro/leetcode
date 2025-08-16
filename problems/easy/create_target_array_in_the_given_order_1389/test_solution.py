import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, nums, index, expected, timeout", [
        ('create_target_array', [0, 1, 2, 3, 4], [0, 1, 2, 2, 1], [0, 4, 1, 3, 2], None),
        ('create_target_array', [1, 2, 3, 4, 0], [0, 1, 2, 3, 0], [0, 1, 2, 3, 4], None),
        ('create_target_array', [1], [0], [1], None),
    ])
    def test_create_target_array(self, method_name, nums, index, expected, timeout):
        self._run_test(self.solution, method_name, (nums, index,), expected, timeout)
