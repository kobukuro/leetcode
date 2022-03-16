# Linked List, Recursion
# reference:https://www.youtube.com/watch?v=XIdigk956u0
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time:O(n+m), Space:O(1)
# Time:O(n+m):因為假如當smaller list的最後一個值是所有值裡最大的, 那還是要把list1以及list2都traverse過
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1 is None and list2 is None:
            return None
        first_ptr = list1
        second_ptr = list2
        dummy = ListNode()
        curr = dummy
        while first_ptr and second_ptr:
            # print(f'first_ptr:{first_ptr}')
            # print(f'second_ptr:{second_ptr}')
            if first_ptr.val < second_ptr.val:
                curr.next = first_ptr
                curr = curr.next
                first_ptr = first_ptr.next
            else:
                curr.next = second_ptr
                curr = curr.next
                second_ptr = second_ptr.next
        if first_ptr:
            curr.next = first_ptr
        if second_ptr:
            curr.next = second_ptr
        return dummy.next
