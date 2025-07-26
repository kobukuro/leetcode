import pytest
from .solution import Solution
from tests.base_test import BaseTestSolution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, coins, amount, expected, timeout", [
        ('coin_change_memoization', [1, 2, 5], 11, 3, BaseTestSolution.DEFAULT_TIMEOUT),
        ('coin_change_memoization', [2], 3, -1, BaseTestSolution.DEFAULT_TIMEOUT),
        ('coin_change_memoization', [1], 0, 0, BaseTestSolution.DEFAULT_TIMEOUT),
        ('coin_change_memoization', [1, 2, 5], 100, 20, BaseTestSolution.DEFAULT_TIMEOUT),
        ('coin_change_dp', [1, 2, 5], 11, 3, BaseTestSolution.DEFAULT_TIMEOUT),
        ('coin_change_dp', [2], 3, -1, BaseTestSolution.DEFAULT_TIMEOUT),
        ('coin_change_dp', [1], 0, 0, BaseTestSolution.DEFAULT_TIMEOUT),
        ('coin_change_dp', [1, 2, 5], 100, 20, BaseTestSolution.DEFAULT_TIMEOUT),
    ])
    def test_num_islands(self, method_name, coins, amount, expected, timeout):
        self._run_test(self.solution, method_name, (coins, amount,), expected, timeout)
