from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "Let's take LeetCode contest"
        res = self.solution.reverse_words(s)
        assert res == "s'teL ekat edoCteeL tsetnoc"

    def test_example_2(self):
        s = "Mr Ding"
        res = self.solution.reverse_words(s)
        assert res == "rM gniD"
