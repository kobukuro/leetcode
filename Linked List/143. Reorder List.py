# Linked List, Two Pointers, Stack, Recursion
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity: O(N). There are three steps here.
# To identify the middle node takes O(N) time.
# To reverse the second part of the list,
# one needs N/2 operations.
# The final step, to merge two lists, requires N/2 operations as well.
# In total, that results in O(N) time complexity.
# Space complexity: O(1), since we do not allocate any additional data structures.
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        p1 = head
        p2 = prev
        while p2.next:
            n1 = p1.next
            p1.next = p2
            p1 = n1
            n2 = p2.next
            p2.next = p1
            p2 = n2
