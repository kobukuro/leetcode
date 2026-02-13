import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, num, expected, timeout", [
        ('maximum69_number', 9669, 9969, None),
        ('maximum69_number', 9996, 9999, None),
        ('maximum69_number', 9999, 9999, None),
    ])
    def test_maximum69_number(self, method_name, num, expected, timeout):
        self._run_test(self.solution, method_name, (num,), expected, timeout)
