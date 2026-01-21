import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, hours, target, expected, timeout", [
        ('number_of_employees_who_met_target', [0, 1, 2, 3, 4], 2, 3, None),
        ('number_of_employees_who_met_target', [5, 1, 4, 2, 2], 6, 0, None),
    ])
    def test_number_of_employees_who_met_target(self, method_name, hours, target, expected, timeout):
        self._run_test(self.solution, method_name, (hours, target,), expected, timeout)
