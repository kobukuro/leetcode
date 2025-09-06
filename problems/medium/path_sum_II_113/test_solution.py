from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(val=5,
                        left=TreeNode(val=4,
                                      left=TreeNode(val=11,
                                                    left=TreeNode(val=7,
                                                                  left=None,
                                                                  right=None),
                                                    right=TreeNode(val=2,
                                                                   left=None,
                                                                   right=None)),
                                      right=None),
                        right=TreeNode(val=8,
                                       left=TreeNode(val=13,
                                                     left=None,
                                                     right=None),
                                       right=TreeNode(val=4,
                                                      left=TreeNode(val=5,
                                                                    left=None,
                                                                    right=None),
                                                      right=TreeNode(val=1,
                                                                     left=None,
                                                                     right=None))))
        target_sum = 22
        expected = [[5, 4, 11, 2], [5, 8, 4, 5]]
        result = self.solution.path_sum(root=root, target_sum=target_sum)
        assert sorted(result) == sorted(expected)

    def test_example_2(self):
        root = TreeNode(val=1,
                        left=TreeNode(val=2),
                        right=TreeNode(val=3))
        target_sum = 5
        expected = []
        assert self.solution.path_sum(root=root, target_sum=target_sum) == expected

    def test_example_3(self):
        root = TreeNode(val=1,
                        left=TreeNode(val=2),
                        right=None)
        target_sum = 0
        expected = []
        assert self.solution.path_sum(root=root, target_sum=target_sum) == expected

    def test_example_4(self):
        root = TreeNode(val=1,
                        left=TreeNode(val=2),
                        right=None)
        target_sum = 1
        expected = []
        assert self.solution.path_sum(root=root, target_sum=target_sum) == expected
