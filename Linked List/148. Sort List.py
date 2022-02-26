# Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # split into two halves
        left = head
        right = self.find_mid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge_two_sorted_linked_list(left, right)

    def find_mid(self, head):
        slow, fast = head, head.next  # fast為head.next, 所以這個function回傳的就會直接是first middle node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_two_sorted_linked_list(self, list1, list2):
        if list1 is None and list2 is not None:
            return list2
        if list2 is None and list1 is not None:
            return list1
        if list1 is None and list2 is None:
            return None
        dummy = ListNode()
        curr = dummy
        fir_ptr = list1
        sec_str = list2
        while fir_ptr and sec_str:
            if fir_ptr.val < sec_str.val:
                curr.next = fir_ptr
                curr = curr.next
                fir_ptr = fir_ptr.next
            else:
                curr.next = sec_str
                curr = curr.next
                sec_str = sec_str.next
        if fir_ptr:
            curr.next = fir_ptr
        if sec_str:
            curr.next = sec_str
        return dummy.next
