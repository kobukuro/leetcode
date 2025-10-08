import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, paths, expected, timeout", [
        ('dest_city', [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]], "Sao Paulo", None),
        ('dest_city', [["B", "C"], ["D", "B"], ["C", "A"]], "A", None),
        ('dest_city', [["A", "Z"]], "Z", None),
    ])
    def test_dest_city(self, method_name, paths, expected, timeout):
        self._run_test(self.solution, method_name, (paths,), expected, timeout)
