import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, allowed, words, expected, timeout", [
        ('count_consistent_strings', "ab", ["ad", "bd", "aaab", "baa", "badab"], 2, None),
        ('count_consistent_strings', "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7, None),
        ('count_consistent_strings', "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4, None),
    ])
    def test_count_consistent_strings(self, method_name, allowed, words, expected, timeout):
        self._run_test(self.solution, method_name, (allowed, words,), expected, timeout)
