import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, words, x, expected, timeout", [
        ('find_words_containing', ["leet", "code"], "e", [0, 1], None),
        ('find_words_containing', ["abc", "bcd", "aaaa", "cbc"], "a", [0, 2], None),
        ('find_words_containing', ["abc", "bcd", "aaaa", "cbc"], "z", [], None),
    ])
    def test_find_words_containing(self, method_name, words, x, expected, timeout):
        self._run_test(self.solution, method_name, (words, x,), expected, timeout)
