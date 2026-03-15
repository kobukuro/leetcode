import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, num, expected, timeout", [
        ('remove_trailing_zeros', "51230000", "5123", None),
        ('remove_trailing_zeros', "123", "123", None),
        ('remove_trailing_zeros', "9", "9", None),
    ])
    def test_remove_trailing_zeros(self, method_name, num, expected, timeout):
        self._run_test(self.solution, method_name, (num,), expected, timeout)
