import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, n, expected, timeout", [
        ('fib_memoization', 2, 1, None),
        ('fib_memoization', 3, 2, None),
        ('fib_memoization', 4, 3, None),
        ('fib_dp', 2, 1, None),
        ('fib_dp', 3, 2, None),
        ('fib_dp', 4, 3, None),
    ])
    def test_fib(self, method_name, n, expected, timeout):
        self._run_test(self.solution, method_name, (n,), expected, timeout)
