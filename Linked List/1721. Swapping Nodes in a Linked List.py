# Linked List, Two Pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        def find_k_from_start(head, k):
            curr = head
            for i in range(k):
                curr = curr.next
            return curr

        def find_k_from_end(head, k):
            n = 0
            curr = head
            while curr:
                n += 1
                curr = curr.next
            # print(n)
            curr = head
            for i in range(n - k):
                curr = curr.next
            return curr

        kth_node = find_k_from_start(dummy, k)
        # print(kth_node.val)
        kth_minus_one_node = find_k_from_start(dummy, k - 1)
        # print(kth_minus_one_node.val)
        kth_plus_one_node = find_k_from_start(dummy, k + 1)
        # print(kth_plus_one_node)
        kth_node_from_end = find_k_from_end(dummy, k)
        # print(kth_node_from_end.val)
        kth_node_minus_one_from_end = find_k_from_end(dummy, k - 1)
        # print(kth_node_minus_one_from_end.val)
        kth_node_plus_one_from_end = find_k_from_end(dummy, k + 1)
        # print(kth_node_plus_one_from_end.val)
        if kth_node.next == kth_node_from_end:
            kth_minus_one_node.next = kth_node_from_end
            kth_node_from_end.next = kth_node
            kth_node.next = kth_node_minus_one_from_end
        elif kth_node_from_end.next == kth_node:
            kth_node_plus_one_from_end.next = kth_node
            kth_node.next = kth_node_from_end
            kth_node_from_end.next = kth_plus_one_node
        else:
            kth_minus_one_node.next = kth_node_from_end
            kth_node_from_end.next = kth_plus_one_node
            kth_node_plus_one_from_end.next = kth_node
            kth_node.next = kth_node_minus_one_from_end
        return dummy.next
