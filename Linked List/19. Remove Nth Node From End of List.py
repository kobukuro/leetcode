# Linked List, Two Pointers
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# L is the length of linked list
# Time complexity :O(L).
# The algorithm makes two traversal of the list, first to calculate list length L
# and second to find the (L−n) th node.
# There are 2L−n operations and time complexity is O(L).

# Space complexity : O(1).
# We only used constant extra space.
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

        # 使用dummy node來解決刪除第一個node的情況
        dummy = ListNode(-1)
        dummy.next = head
        # 找到倒數第n+1個node
        node = nth_from_end(dummy, n + 1)
        node.next = node.next.next
        return dummy.next
