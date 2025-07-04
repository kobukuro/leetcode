from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "()"
        result = self.solution.is_valid(s)
        assert result

    def test_example_2(self):
        s = "()[]{}"
        result = self.solution.is_valid(s)
        assert result

    def test_example_3(self):
        s = "(]"
        result = self.solution.is_valid(s)
        assert not result

    def test_example_4(self):
        s = "([])"
        result = self.solution.is_valid(s)
        assert result
