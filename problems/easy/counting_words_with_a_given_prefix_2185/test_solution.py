import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, words, pref, expected, timeout", [
        ('prefix_count', ["pay", "attention", "practice", "attend"], "at", 2, None),
        ('prefix_count', ["leetcode", "win", "loops", "success"], "code", 0, None),
    ])
    def test_prefix_count(self, method_name, words, pref, expected, timeout):
        self._run_test(self.solution, method_name, (words, pref,), expected, timeout)
