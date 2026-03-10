import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, k, expected, timeout", [
        ('truncate_sentence', "Hello how are you Contestant", 4, "Hello how are you", None),
        ('truncate_sentence', "What is the solution to this problem", 4, "What is the solution", None),
        ('truncate_sentence', "chopper is not a tanuki", 5, "chopper is not a tanuki", None),
    ])
    def test_truncate_sentence(self, method_name, s, k, expected, timeout):
        self._run_test(self.solution, method_name, (s, k,), expected, timeout)
