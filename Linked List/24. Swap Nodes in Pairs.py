# Linked List, Recursion
# Difficult
# reference:https://www.youtube.com/watch?v=o811TZLAWOo
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save pointers
            next_pair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = next_pair
            prev.next = second

            # update pointers
            prev = curr
            curr = next_pair
        return dummy.next
