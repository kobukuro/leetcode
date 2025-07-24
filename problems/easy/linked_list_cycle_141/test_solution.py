from .solution import Solution
from utils.data_structures import ListNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1_two_pointers(self):
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        assert self.solution.has_cycle_two_pointers(node1)

    def test_example_1_two_pointers(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1
        assert self.solution.has_cycle_two_pointers(node1)

    def test_example_3_two_pointers(self):
        node1 = ListNode(1)
        assert not self.solution.has_cycle_two_pointers(node1)

    def test_example_1_hash_table(self):
        node1 = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2
        assert self.solution.has_cycle_hash_set(node1)

    def test_example_2_hash_table(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2
        node2.next = node1
        assert self.solution.has_cycle_hash_set(node1)

    def test_example_3_hash_table(self):
        node1 = ListNode(1)
        assert not self.solution.has_cycle_hash_set(node1)
