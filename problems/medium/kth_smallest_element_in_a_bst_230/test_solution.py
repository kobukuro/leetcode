from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(val=3,
                        left=TreeNode(val=1,
                                      right=TreeNode(val=2)),
                        right=TreeNode(val=4))
        k = 1
        expected = 1
        assert self.solution.kth_smallest(root=root, k=k) == expected

    def test_example_2(self):
        root = TreeNode(val=5,
                        left=TreeNode(val=3,
                                      left=TreeNode(val=2,
                                                    left=TreeNode(val=1)),
                                      right=TreeNode(val=4)),
                        right=TreeNode(val=6))
        k = 3
        expected = 3
        assert self.solution.kth_smallest(root=root, k=k) == expected
