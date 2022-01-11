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
