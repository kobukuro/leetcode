# Linked List, Two Pointers
# reference:https://www.youtube.com/watch?v=UcGtPs2LE_c
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        length = 0
        while curr.next is not None:
            length += 1
            curr = curr.next
        length += 1
        tail = curr
        k = k % length
        if k == 0:
            return head
        moves = length - k - 1
        pos = head
        for i in range(moves):
            pos = pos.next
        new_head = pos.next
        pos.next = None
        tail.next = head
        return new_head
