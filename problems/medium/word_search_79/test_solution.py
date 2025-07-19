import pytest
from .solution import Solution
from tests.base_test import BaseTestSolution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, board, word, expected, timeout", [
        ('exist', [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True, None),
        ('exist', [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True, None),
        ('exist', [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False, None)
    ])
    def test_num_islands(self, method_name, board, word, expected, timeout):
        self._run_test(self.solution, method_name, (board, word,), expected, timeout)
