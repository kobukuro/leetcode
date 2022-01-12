# Linked List, Two Pointers, Stack, Recursion
# reference:https://www.youtube.com/watch?v=yOzXms1J6Nk
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        l, r = 0, len(arr) - 1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True


# Space O(1)
class BetterSolution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        # idea: when fast pointer reaches end, slow pointer will be middle
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse second half of linked list
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # check palindrome
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True


if __name__ == '__main__':
    head = ListNode(val=1, next=ListNode(val=2,
                                         next=ListNode(val=2,
                                                       next=ListNode(val=1))))
    print(BetterSolution().isPalindrome(head=head))
