# Hash Table, Linked List, Two Pointers
# reference:https://labuladong.gitee.io/algo/2/18/17/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1 is not None:
                p1 = p1.next
            else:
                p1 = headB
            if p2 is not None:
                p2 = p2.next
            else:
                p2 = headA
        return p1
