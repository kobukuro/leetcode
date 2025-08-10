import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, words, chars, expected, timeout", [
        ('count_characters', ["cat", "bt", "hat", "tree"], "atach", 6, None),
        ('count_characters', ["hello", "world", "leetcode"], "welldonehoneyr", 10, None),
    ])
    def test_count_characters(self, method_name, words, chars, expected, timeout):
        self._run_test(self.solution, method_name, (words, chars,), expected, timeout)
