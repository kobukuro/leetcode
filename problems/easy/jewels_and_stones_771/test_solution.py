import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, jewels, stones, expected, timeout", [
        ('num_jewels_in_stones', "aA", "aAAbbbb", 3, None),
        ('num_jewels_in_stones', "z", "ZZ", 0, None),
    ])
    def test_num_jewels_in_stones(self, method_name, jewels, stones, expected, timeout):
        self._run_test(self.solution, method_name, (jewels, stones,), expected, timeout)
