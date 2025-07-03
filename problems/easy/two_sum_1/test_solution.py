from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected1 = [0, 1]
        expected2 = [1, 0]
        assert self.solution.two_sum(nums, target) == expected1 or self.solution.two_sum(nums, target) == expected2

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected1 = [1, 2]
        expected2 = [2, 1]
        assert self.solution.two_sum(nums, target) == expected1 or self.solution.two_sum(nums, target) == expected2

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected1 = [0, 1]
        expected2 = [1, 0]
        assert self.solution.two_sum(nums, target) == expected1 or self.solution.two_sum(nums, target) == expected2
