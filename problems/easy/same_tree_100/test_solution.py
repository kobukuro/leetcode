from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        p = TreeNode(val=1,
                     left=TreeNode(val=2),
                     right=TreeNode(val=3))
        q = TreeNode(val=1,
                     left=TreeNode(val=2),
                     right=TreeNode(val=3))
        assert self.solution.is_same_tree(p=p, q=q)

    def test_example_2(self):
        p = TreeNode(val=1,
                     left=TreeNode(val=2))
        q = TreeNode(val=1,
                     right=TreeNode(val=2))
        assert not self.solution.is_same_tree(p=p, q=q)

    def test_example_3(self):
        p = TreeNode(val=1,
                     left=TreeNode(val=2),
                     right=TreeNode(val=1))
        q = TreeNode(val=1,
                     left=TreeNode(val=1),
                     right=TreeNode(val=2))
        assert not self.solution.is_same_tree(p=p, q=q)
