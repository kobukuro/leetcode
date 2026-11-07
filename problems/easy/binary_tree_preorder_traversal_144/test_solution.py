from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        # root = [1,null,2,3]
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        assert self.solution.preorder_traversal(root) == [1, 2, 3]

    def test_example_2(self):
        # root = [1,2,3,4,5,null,8,null,null,6,7,9]
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, None, TreeNode(8, TreeNode(9))),
        )
        assert self.solution.preorder_traversal(root) == [1, 2, 4, 5, 6, 7, 3, 8, 9]

    def test_example_3(self):
        # root = []
        assert self.solution.preorder_traversal(None) == []

    def test_example_4(self):
        # root = [1]
        assert self.solution.preorder_traversal(TreeNode(1)) == [1]
