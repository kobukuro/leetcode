from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(val=5,
                        left=TreeNode(val=4,
                                      left=TreeNode(val=11,
                                                    left=TreeNode(val=7),
                                                    right=TreeNode(val=2))),
                        right=TreeNode(val=8,
                                       left=TreeNode(val=13),
                                       right=TreeNode(val=4,
                                                      right=TreeNode(val=1))))
        target_sum = 22
        assert self.solution.has_path_sum(root=root, target_sum=target_sum)

    def test_example_2(self):
        root = TreeNode(val=1,
                        left=TreeNode(val=2),
                        right=TreeNode(val=3))
        target_sum = 5
        assert not self.solution.has_path_sum(root=root, target_sum=target_sum)

    def test_example_3(self):
        root = None
        target_sum = 0
        assert not self.solution.has_path_sum(root=root, target_sum=target_sum)
