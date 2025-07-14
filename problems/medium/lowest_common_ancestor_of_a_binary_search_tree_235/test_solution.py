from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(val=6,
                        left=TreeNode(val=2,
                                      left=TreeNode(val=0),
                                      right=TreeNode(val=4,
                                                     left=TreeNode(val=3),
                                                     right=TreeNode(val=5))),
                        right=TreeNode(val=8,
                                       left=TreeNode(val=7),
                                       right=TreeNode(val=9)))
        p = TreeNode(val=2)
        q = TreeNode(val=8)
        assert self.solution.lowest_common_ancestor(root=root, p=p, q=q).val == 6

    def test_example_2(self):
        root = TreeNode(val=6,
                        left=TreeNode(val=2,
                                      left=TreeNode(val=0),
                                      right=TreeNode(val=4,
                                                     left=TreeNode(val=3),
                                                     right=TreeNode(val=5))),
                        right=TreeNode(val=8,
                                       left=TreeNode(val=7),
                                       right=TreeNode(val=9)))
        p = TreeNode(val=2)
        q = TreeNode(val=4)
        assert self.solution.lowest_common_ancestor(root=root, p=p, q=q).val == 2

    def test_example_3(self):
        root = TreeNode(val=2,
                        left=TreeNode(val=1))
        p = TreeNode(val=2)
        q = TreeNode(val=1)
        assert self.solution.lowest_common_ancestor(root=root, p=p, q=q).val == 2
