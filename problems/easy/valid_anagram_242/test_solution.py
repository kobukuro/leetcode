import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, t, expected, timeout", [
        ('is_anagram', "anagram", "nagaram", True, None),
        ('is_anagram', "rat", "car", False, None),
    ])
    def test_is_anagram(self, method_name, s, t, expected, timeout):
        self._run_test(self.solution, method_name, (s, t,), expected, timeout)
