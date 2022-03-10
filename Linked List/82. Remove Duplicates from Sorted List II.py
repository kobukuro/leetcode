# Linked List, Two Pointers
# reference:https://www.youtube.com/watch?v=UESeImUsUdw
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                val = curr.val
                while curr is not None and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        return dummy.next
