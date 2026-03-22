from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test from LeetCode example 1"""
        nums = [1, 1, 2]
        expected_k = 2
        expected_nums = [1, 2]

        k = self.solution.remove_duplicates(nums)

        assert k == expected_k
        assert nums[:k] == expected_nums

    def test_example_2(self):
        """Test from LeetCode example 2"""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_k = 5
        expected_nums = [0, 1, 2, 3, 4]

        k = self.solution.remove_duplicates(nums)

        assert k == expected_k
        assert nums[:k] == expected_nums
