import pytest
from tests.base_test import BaseTestSolution
from .solution import Solution


class TestSolution(BaseTestSolution):
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_example_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        assert nums1 == [1]

    def test_example_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.solution.merge(nums1, m, nums2, n)
        assert nums1 == [1]

    def test_example_4(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_example_5(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [4, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 3, 4, 5, 6]
