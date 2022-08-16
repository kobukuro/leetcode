# Linked List, Simulation
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(val=-1)
        res_curr = res
        curr = head
        temp = None
        while curr:
            # print(temp)
            if curr.val == 0 and temp is not None:
                new_node = ListNode(val=temp)
                res_curr.next = new_node
                res_curr = res_curr.next
                temp = None
            elif curr.val != 0:
                if temp is None:
                    temp = curr.val
                else:
                    temp += curr.val
            curr = curr.next
        return res.next
