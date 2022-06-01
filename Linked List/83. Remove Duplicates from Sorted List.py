# Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=101, next=head)
        prev = dummy
        curr = head
        while curr:
            if prev.val == curr.val:
                while curr and prev.val == curr.val:
                    curr = curr.next
                prev.next = curr
                prev = prev.next
                if curr:
                    curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next
