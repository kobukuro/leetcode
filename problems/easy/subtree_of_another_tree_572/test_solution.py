from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3,
                        TreeNode(4,
                                 TreeNode(1),
                                 TreeNode(2)),
                        TreeNode(5))
        sub_root = TreeNode(4,
                            TreeNode(1),
                            TreeNode(2))
        assert self.solution.is_subtree(root, sub_root)

    def test_example_2(self):
        root = TreeNode(3,
                        TreeNode(4,
                                 TreeNode(1),
                                 TreeNode(2,
                                          TreeNode(0))),
                        TreeNode(5))
        sub_root = TreeNode(4,
                            TreeNode(1),
                            TreeNode(2))
        assert not self.solution.is_subtree(root, sub_root)
