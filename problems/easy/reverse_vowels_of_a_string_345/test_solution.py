import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('reverse_vowels', "IceCreAm", "AceCreIm", None),
        ('reverse_vowels', "leetcode", "leotcede", None),
        ('reverse_vowels', ".,", ".,", None),
    ])
    def test_reverse_vowels(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
