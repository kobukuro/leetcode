from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        assert self.solution.contains_duplicate(nums) is True

    def test_example_2(self):
        nums = [1, 2, 3, 4]
        assert self.solution.contains_duplicate(nums) is False

    def test_example_3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        assert self.solution.contains_duplicate(nums) is True
