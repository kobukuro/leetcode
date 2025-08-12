import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, candies, extra_candies, expected, timeout", [
        ('kids_with_candies', [2, 3, 5, 1, 3], 3, [True, True, True, False, True], None),
        ('kids_with_candies', [4, 2, 1, 1, 2], 1, [True, False, False, False, False], None),
        ('kids_with_candies', [12, 1, 12], 10, [True, False, True], None),
    ])
    def test_kids_with_candies(self, method_name, candies, extra_candies, expected, timeout):
        self._run_test(self.solution, method_name, (candies, extra_candies,), expected, timeout)
