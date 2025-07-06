import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, n, expected, timeout", [
        ('climb_stairs_memoization', 2, 2, None),
        ('climb_stairs_memoization', 3, 3, None),
        ('climb_stairs_memoization', 38, 63245986, BaseTestSolution.DEFAULT_TIMEOUT),
        ('climb_stairs_dp', 2, 2, None),
        ('climb_stairs_dp', 3, 3, None),
        ('climb_stairs_dp', 38, 63245986, BaseTestSolution.DEFAULT_TIMEOUT),
    ])
    def test_climb_stairs(self, method_name, n, expected, timeout):
        self._run_test(TestSolution.solution, method_name, (n,), expected, timeout)
