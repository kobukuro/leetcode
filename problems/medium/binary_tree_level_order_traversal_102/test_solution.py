from .solution import Solution
from utils.data_structures import TreeNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(val=3,
                        left=TreeNode(val=9),
                        right=TreeNode(val=20,
                                       left=TreeNode(val=15),
                                       right=TreeNode(val=7)))
        expected = [[3], [9, 20], [15, 7]]
        assert self.solution.level_order(root=root) == expected

    def test_example_2(self):
        root = TreeNode(val=1)
        expected = [[1]]
        assert self.solution.level_order(root=root) == expected

    def test_example_3(self):
        root = None
        expected = []
        assert self.solution.level_order(root=root) == expected
