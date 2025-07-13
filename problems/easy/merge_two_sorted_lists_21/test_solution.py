from .solution import Solution
from utils.data_structures import ListNode


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        list1 = ListNode(val=1,
                         next=ListNode(val=2,
                                       next=ListNode(val=4)))
        list2 = ListNode(val=1,
                         next=ListNode(val=3,
                                       next=ListNode(val=4)))
        merged_list = self.solution.merge_two_lists(list1=list1, list2=list2)
        assert merged_list.val == 1
        assert merged_list.next.val == 1
        assert merged_list.next.next.val == 2
        assert merged_list.next.next.next.val == 3
        assert merged_list.next.next.next.next.val == 4
        assert merged_list.next.next.next.next.next.val == 4
        assert merged_list.next.next.next.next.next.next is None

    def test_example_2(self):
        list1 = None
        list2 = None
        merged_list = self.solution.merge_two_lists(list1=list1, list2=list2)
        assert merged_list is None

    def test_example_3(self):
        list1 = None
        list2 = ListNode(val=0)
        merged_list = self.solution.merge_two_lists(list1=list1, list2=list2)
        assert merged_list.val == 0
        assert merged_list.next is None
