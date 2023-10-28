from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        # print(values)
        res = 0
        l = 0
        r = len(values) - 1
        while l < r:
            res = max(res, values[l] + values[r])
            l += 1
            r -= 1
        return res
