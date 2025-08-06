import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, celsius, expected, timeout", [
        ('convert_temperature', 36.50, [309.65000, 97.70000], None),
        ('convert_temperature', 122.11, [395.26000, 251.79800], None),
    ])
    def test_convert_temperature(self, method_name, celsius, expected, timeout):
        self._run_test(self.solution, method_name, (celsius,), expected, timeout)
