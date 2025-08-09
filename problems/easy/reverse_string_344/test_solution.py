from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        s = ["h", "e", "l", "l", "o"]
        self.solution.reverse_string(s)
        assert s == ["o", "l", "l", "e", "h"]

    def test_example_2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        self.solution.reverse_string(s)
        assert s == ["h", "a", "n", "n", "a", "H"]
