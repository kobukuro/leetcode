import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, ransom_note, magazine, expected, timeout", [
        ('can_construct', "a", "b", False, None),
        ('can_construct', "aa", "ab", False, None),
        ('can_construct', "aa", "aab", True, None),
    ])
    def test_can_construct(self, method_name, ransom_note, magazine, expected, timeout):
        self._run_test(self.solution, method_name, (ransom_note, magazine,), expected, timeout)
