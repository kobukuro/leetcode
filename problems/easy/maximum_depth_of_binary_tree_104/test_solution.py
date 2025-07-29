from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3,
                        TreeNode(9),
                        TreeNode(20,
                                 TreeNode(15),
                                 TreeNode(7)))
        assert self.solution.max_depth(root) == 3

    def test_example_2(self):
        root = TreeNode(1,
                        None,
                        TreeNode(2))
        assert self.solution.max_depth(root) == 2
