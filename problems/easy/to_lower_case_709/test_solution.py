import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('to_lower_case', "Hello", "hello", None),
        ('to_lower_case', "here", "here", None),
        ('to_lower_case', "LOVELY", "lovely", None),
    ])
    def test_to_lower_case(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
