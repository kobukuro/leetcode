from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [-4, -1, 0, 3, 10]
        expected = [0, 1, 9, 16, 100]
        assert self.solution.sorted_squares(nums) == expected

    def test_example_2(self):
        nums = [-7, -3, 2, 3, 11]
        expected = [4, 9, 9, 49, 121]
        assert self.solution.sorted_squares(nums) == expected
