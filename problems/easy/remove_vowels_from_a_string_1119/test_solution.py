import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('remove_vowels', "leetcodeisacommunityforcoders", "ltcdscmmntyfrcdrs", None),
        ('remove_vowels', "aeiou", "", None),
    ])
    def test_remove_vowels(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
