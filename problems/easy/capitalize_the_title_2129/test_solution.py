import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, title, expected, timeout", [
        ('capitalize_title', "capiTalIze tHe titLe", "Capitalize The Title", None),
        ('capitalize_title', "First leTTeR of EACH Word", "First Letter of Each Word", None),
        ('capitalize_title', "i lOve leetcode", "i Love Leetcode", None),
    ])
    def test_capitalize_title(self, method_name, title, expected, timeout):
        self._run_test(self.solution, method_name, (title,), expected, timeout)
