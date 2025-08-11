import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, words, expected, timeout", [
        ('unique_morse_representations', ["gin", "zen", "gig", "msg"], 2, None),
        ('unique_morse_representations', ["a"], 1, None),
    ])
    def test_unique_morse_representations(self, method_name, words, expected, timeout):
        self._run_test(self.solution, method_name, (words,), expected, timeout)
