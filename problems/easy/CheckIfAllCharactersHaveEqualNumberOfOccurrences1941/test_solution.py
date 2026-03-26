import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('are_occurrences_equal', "abacbc", True, None),
        ('are_occurrences_equal', "aaabb", False, None),
    ])
    def test_are_occurrences_equal(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
