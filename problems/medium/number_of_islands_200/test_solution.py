import pytest
from .solution import Solution
from tests.base_test import BaseTestSolution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, grid, expected, timeout", [
        ('num_islands_dfs', [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ], 1, None),
        ('num_islands_dfs', [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ], 3, None),
    ])
    def test_num_islands(self, method_name, grid, expected, timeout):
        self._run_test(self.solution, method_name, (grid,), expected, timeout)
