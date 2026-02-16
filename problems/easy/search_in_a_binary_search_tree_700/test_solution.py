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
                        right=TreeNode(val=7))
        val = 2
        expected = root.left
        assert self.solution.search_bst(root, val) == expected

    def test_example_2(self):
        root = TreeNode(val=4,
                        left=TreeNode(val=2,
                                      left=TreeNode(val=1),
                                      right=TreeNode(val=3)),
                        right=TreeNode(val=7))
        val = 5
        expected = None
        assert self.solution.search_bst(root, val) == expected
