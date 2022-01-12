# Linked List, Recursion
# reference:https://www.youtube.com/watch?v=JI71sxtHTng
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: [ListNode], val: int) -> ListNode:
        dummy = ListNode(val=-1, next=head)
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(val=1)
    val = 1
    res = []
    node = Solution().removeElements(head=head, val=val)
    while node:
        res.append(node.val)
        node = node.next
    print(res)
