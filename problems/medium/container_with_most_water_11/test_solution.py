import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, height , expected, timeout", [
        ('max_area', [1, 8, 6, 2, 5, 4, 8, 3, 7], 49, None),
        ('max_area', [1, 1], 1, None),
    ])
    def test_max_area(self, method_name, height, expected, timeout):
        self._run_test(self.solution, method_name, (height,), expected, timeout)
