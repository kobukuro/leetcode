import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, sentences, expected, timeout", [
        ('most_words_found', ["alice and bob love leetcode", "i think so too", "this is great thanks very much"], 6,
         None),
        ('most_words_found', ["please wait", "continue to fight", "continue to win"], 3, None),
    ])
    def test_most_words_found(self, method_name, sentences, expected, timeout):
        self._run_test(self.solution, method_name, (sentences,), expected, timeout)
