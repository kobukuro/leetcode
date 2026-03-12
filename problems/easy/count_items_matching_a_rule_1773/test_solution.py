import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, items, rule_key, rule_value, expected, timeout", [
        ('count_matches', [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
         "color", "silver", 1, None),
        ('count_matches', [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
         "type", "phone", 2, None)])
    def test_count_matches(self, method_name, items, rule_key, rule_value, expected, timeout):
        self._run_test(self.solution, method_name, (items, rule_key, rule_value,), expected, timeout)
