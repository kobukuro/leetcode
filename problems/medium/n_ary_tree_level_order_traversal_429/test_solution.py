from .solution import Solution
from utils.data_structures import Node


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        root = Node(1, [
            Node(3, [Node(5), Node(6)]),
            Node(2),
            Node(4)
        ])
        expected = [[1], [3, 2, 4], [5, 6]]
        assert self.solution.level_order(root) == expected

    def test_example_2(self):
        root = Node(1, [
            Node(2),
            Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
            Node(4, [Node(8, [Node(12)])]),
            Node(5, [Node(9, [Node(13)]), Node(10)])
        ])
        expected = [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]
        assert self.solution.level_order(root) == expected
