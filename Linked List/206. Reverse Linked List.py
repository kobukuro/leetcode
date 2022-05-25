# Linked List, Recursion
# reference:https://www.youtube.com/watch?v=G0_I-ZF0S38
# iterative solution Time O(n), Space O(1)
class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# recursive solution Time O(n),
# Space O(n):The extra space comes from implicit stack space due to recursion.
# The recursion could go up to n levels deep.
class RecursiveSolution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
