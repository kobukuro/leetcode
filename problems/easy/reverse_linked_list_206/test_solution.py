from .solution import Solution
from utils.data_structures import ListNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1_iterative(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        reversed_head = self.solution.reverse_list_iterative(head)
        assert reversed_head.val == 5
        assert reversed_head.next.val == 4
        assert reversed_head.next.next.val == 3
        assert reversed_head.next.next.next.val == 2
        assert reversed_head.next.next.next.next.val == 1
        assert reversed_head.next.next.next.next.next is None

    def test_example_2_iterative(self):
        head = ListNode(1, ListNode(2))
        reversed_head = self.solution.reverse_list_iterative(head)
        assert reversed_head.val == 2
        assert reversed_head.next.val == 1
        assert reversed_head.next.next is None

    def test_example_3_iterative(self):
        head = None
        reversed_head = self.solution.reverse_list_iterative(head)
        assert reversed_head is None

    def test_example_1_recursive(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        reversed_head = self.solution.reverse_list_recursive(head)
        assert reversed_head.val == 5
        assert reversed_head.next.val == 4
        assert reversed_head.next.next.val == 3
        assert reversed_head.next.next.next.val == 2
        assert reversed_head.next.next.next.next.val == 1
        assert reversed_head.next.next.next.next.next is None

    def test_example_2_recursive(self):
        head = ListNode(1, ListNode(2))
        reversed_head = self.solution.reverse_list_recursive(head)
        assert reversed_head.val == 2
        assert reversed_head.next.val == 1
        assert reversed_head.next.next is None

    def test_example_3_recursive(self):
        head = None
        reversed_head = self.solution.reverse_list_recursive(head)
        assert reversed_head is None
