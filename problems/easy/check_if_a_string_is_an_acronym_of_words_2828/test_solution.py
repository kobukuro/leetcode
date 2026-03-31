import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, words, s, expected, timeout", [
        ('is_acronym', ["alice", "bob", "charlie"], "abc", True, None),
        ('is_acronym', ["an", "apple"], "a", False, None),
        ('is_acronym', ["never", "gonna", "give", "up", "on", "you"], "ngguoy", True, None),
    ])
    def test_is_acronym(self, method_name, words, s, expected, timeout):
        self._run_test(self.solution, method_name, (words, s,), expected, timeout)
