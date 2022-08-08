# Linked List, Math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        bit = ''
        while curr:
            bit += str(curr.val)
            curr = curr.next
        return int(bit, 2)
