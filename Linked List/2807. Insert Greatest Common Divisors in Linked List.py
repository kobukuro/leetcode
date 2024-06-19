# Linked List, Math, Number Theory
import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(val=-1)
        curr = head
        while curr.next:
            node = ListNode(val=math.gcd(curr.val, curr.next.val))
            prev.next = curr
            curr = curr.next
            prev.next.next = node
            prev = node
        prev.next = curr
        return dummy.next
