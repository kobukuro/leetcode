import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    solution = Solution()

    @pytest.mark.parametrize("method_name, emails, expected, timeout", [
        ('num_unique_emails',
         ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"], 2,
         None),
        ('num_unique_emails', ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"], 3, None),
    ])
    def test_num_unique_emails(self, method_name, emails, expected, timeout):
        self._run_test(self.solution, method_name, (emails,), expected, timeout)
