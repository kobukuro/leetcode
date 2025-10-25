import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, n, expected, timeout", [
        ('hamming_weight', 11, 3, None),
        ('hamming_weight', 128, 1, None),
        ('hamming_weight', 2147483645, 30, None),
    ])
    def test_hamming_weight(self, method_name, n, expected, timeout):
        self._run_test(self.solution, method_name, (n,), expected, timeout)
