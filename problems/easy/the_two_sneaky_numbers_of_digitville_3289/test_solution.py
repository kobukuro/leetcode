from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [0, 1, 1, 0]
        expected1 = [0, 1]
        expected2 = [1, 0]
        result = self.solution.get_sneaky_numbers(nums)
        assert result in (expected1, expected2)

    def test_example_2(self):
        nums = [0, 3, 2, 1, 3, 2]
        expected1 = [2, 3]
        expected2 = [3, 2]
        result = self.solution.get_sneaky_numbers(nums)
        assert result in (expected1, expected2)

    def test_example_3(self):
        nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
        expected1 = [4, 5]
        expected2 = [5, 4]
        result = self.solution.get_sneaky_numbers(nums)
        assert result in (expected1, expected2)
