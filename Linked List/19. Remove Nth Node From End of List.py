# Linked List, Two Pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reference:https://labuladong.gitee.io/algo/2/18/17/
        # 為了找到倒數第k個node(倒數第一個node不是null),
        # 必須走n-k步(n為node總數, 不包括null node)
        # 走到null需要n步, 所以先讓一個指針先走k步, 在此同時, 讓第二個指針一起開始走
        # 那第二個指針就會走了n-k步
        # 下面這個解法先不用上述方法
        def nth_from_end(head, n):
            total_num = 0
            curr = head
            while curr:
                curr = curr.next
                total_num += 1
            target = head
            for i in range(total_num - n):
                target = target.next
            return target

        print(nth_from_end(head, n).val)
        # 使用dummy node來解決刪除第一個node的情況
        dummy = ListNode(-1)
        dummy.next = head
        # 找到倒數第n+1個node
        node = nth_from_end(dummy, n + 1)
        node.next = node.next.next
        return dummy.next
