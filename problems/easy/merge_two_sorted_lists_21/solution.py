# Tags: Linked List
from typing import Optional
from utils.data_structures import ListNode


class Solution:
    # Time complexity: O(n + m), where n and m are the lengths of the two linked lists.
    # Because if the last value of the shorter list is the largest among all the values, we still need to traverse both list1 and list2.
    # Space complexity: O(1)
    def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        return dummy.next
