# Linked List, Math, Recursion
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        curr = dummy_node
        ptr1 = l1
        ptr2 = l2
        add_one = False
        while ptr1 and ptr2:
            if add_one:
                val = ptr1.val + ptr2.val + 1
            else:
                val = ptr1.val + ptr2.val
            if val >= 10:
                add_one = True
            else:
                add_one = False
            new_node = ListNode(val=int(str(val)[-1]))
            curr.next = new_node
            curr = curr.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if not add_one:
            if ptr1:
                new_node.next = ptr1
            if ptr2:
                new_node.next = ptr2
        else:
            while ptr1:
                if add_one:
                    val = ptr1.val + 1
                else:
                    val = ptr1.val
                if val >= 10:
                    add_one = True
                else:
                    add_one = False
                new_node = ListNode(val=int(str(val)[-1]))
                curr.next = new_node
                curr = curr.next
                ptr1 = ptr1.next
            while ptr2:
                if add_one:
                    val = ptr2.val + 1
                else:
                    val = ptr2.val
                if val >= 10:
                    add_one = True
                else:
                    add_one = False
                new_node = ListNode(val=int(str(val)[-1]))
                curr.next = new_node
                curr = curr.next
                ptr2 = ptr2.next
        if add_one:
            new_node = ListNode(1)
            curr.next = new_node
        return dummy_node.next
