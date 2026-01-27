import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, operations, expected, timeout", [
        ('final_value_after_operations', ["--X", "X++", "X++"], 1, None),
        ('final_value_after_operations', ["++X", "++X", "X++"], 3, None),
        ('final_value_after_operations', ["X++", "++X", "--X", "X--"], 0, None),
    ])
    def test_final_value_after_operations(self, method_name, operations, expected, timeout):
        self._run_test(self.solution, method_name, (operations,), expected, timeout)
