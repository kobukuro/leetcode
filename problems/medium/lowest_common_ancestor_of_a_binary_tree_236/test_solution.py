from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3,
                        left=TreeNode(5,
                                      left=TreeNode(6),
                                      right=TreeNode(2,
                                                     left=TreeNode(7),
                                                     right=TreeNode(4))),
                        right=TreeNode(1,
                                       left=TreeNode(0),
                                       right=TreeNode(8)))
        p = root.left  # Node with value 5
        q = root.right  # Node with value 1
        assert self.solution.lowest_common_ancestor(root, p, q) == root

    def test_example_2(self):
        root = TreeNode(3,
                        left=TreeNode(5,
                                      left=TreeNode(6),
                                      right=TreeNode(2,
                                                     left=TreeNode(7),
                                                     right=TreeNode(4))),
                        right=TreeNode(1,
                                       left=TreeNode(0),
                                       right=TreeNode(8)))
        p = root.left
        q = root.left.right.right
        assert self.solution.lowest_common_ancestor(root, p, q) == p

    def test_example_3(self):
        root = TreeNode(1,
                        left=TreeNode(2))
        p = root
        q = root.left
        assert self.solution.lowest_common_ancestor(root, p, q) == root
