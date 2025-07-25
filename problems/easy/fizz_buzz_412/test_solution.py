import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, n, expected, timeout", [
        ('fizz_buzz', 3, ["1", "2", "Fizz"], None),
        ('fizz_buzz', 5, ["1", "2", "Fizz", "4", "Buzz"], None),
        ('fizz_buzz', 15,
         ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"], None),
    ])
    def test_fib(self, method_name, n, expected, timeout):
        self._run_test(self.solution, method_name, (n,), expected, timeout)
