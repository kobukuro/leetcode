import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, s, expected, timeout", [
        ('first_uniq_char', "leetcode", 0, None),
        ('first_uniq_char', "loveleetcode", 2, None),
        ('first_uniq_char', "aabb", -1, None),
    ])
    def test_first_uniq_char(self, method_name, s, expected, timeout):
        self._run_test(self.solution, method_name, (s,), expected, timeout)
