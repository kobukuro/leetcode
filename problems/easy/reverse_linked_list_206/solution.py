# Tags: Linked List
from typing import Optional
from utils.data_structures import ListNode


class Solution:
    # Time complexity : O(n), where n is the list's length.
    # Space complexity : O(1).
    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    # Time complexity : O(n), where n is the list's length.
    # Space complexity : O(n).
    # The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.
    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head
