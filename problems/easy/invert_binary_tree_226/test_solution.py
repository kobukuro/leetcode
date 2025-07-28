from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(val=4,
                        left=TreeNode(val=2,
                                      left=TreeNode(val=1),
                                      right=TreeNode(val=3)),
                        right=TreeNode(val=7,
                                       left=TreeNode(val=6),
                                       right=TreeNode(val=9)))
        inverted_root = self.solution.invert_tree(root)
        assert inverted_root.val == 4
        assert inverted_root.left.val == 7
        assert inverted_root.right.val == 2
        assert inverted_root.left.left.val == 9
        assert inverted_root.left.right.val == 6
        assert inverted_root.right.left.val == 3
        assert inverted_root.right.right.val == 1
        assert inverted_root.left.left.left is None
        assert inverted_root.left.left.right is None
        assert inverted_root.left.right.left is None
        assert inverted_root.left.right.right is None
        assert inverted_root.right.left.left is None
        assert inverted_root.right.left.right is None
        assert inverted_root.right.right.left is None
        assert inverted_root.right.right.right is None

    def test_example_2(self):
        root = TreeNode(val=2,
                        left=TreeNode(val=1),
                        right=TreeNode(val=3))
        inverted_root = self.solution.invert_tree(root)
        assert inverted_root.val == 2
        assert inverted_root.left.val == 3
        assert inverted_root.right.val == 1
        assert inverted_root.left.left is None
        assert inverted_root.left.right is None
        assert inverted_root.right.left is None
        assert inverted_root.right.right is None

    def test_example_3(self):
        root = None
        inverted_root = self.solution.invert_tree(root)
        assert inverted_root is None
