from .solution import Solution


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4, 6]
        result = self.solution.find_difference(nums1, nums2)
        assert len(result) == 2
        assert set(result[0]) == {1, 3}
        assert set(result[1]) == {4, 6}

    def test_example_2(self):
        nums1 = [1, 2, 3, 3]
        nums2 = [1, 1, 2, 2]
        result = self.solution.find_difference(nums1, nums2)
        assert len(result) == 2
        assert set(result[0]) == {3}
        assert set(result[1]) == set()
