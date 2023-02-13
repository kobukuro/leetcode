# Linked List, Divide and Conquer, Heap(Priority Queue), Merge Sort
# reference:https://www.youtube.com/watch?v=q5a5OiGbT6Q
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from heapq import heappush, heappop


# reference:https://www.youtube.com/watch?v=RCuBc4Zl-oY
# reference:https://www.youtube.com/watch?v=ptYUCjfNhJY
# Time complexity : O(N log k) where k is the number of linked lists.
# The comparison cost will be reduced to O(log k) for every pop and insertion to heap.
# But finding the node with the smallest value just costs O(1) time.
# There are N nodes in the final linked list.

# Space complexity :
# O(n) Creating a new linked list costs O(n) space.
# O(k) The code above present applies in-place method which cost O(1) space.
# And the heap costs O(k) space (it's far less than N in most situations).
class HeapSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for index, l in enumerate(lists):
            if l:
                heappush(min_heap, (l.val, index))
        dummy = curr = ListNode()
        while min_heap:
            val, i = heappop(min_heap)
            curr.next = ListNode(val=val)
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heappush(min_heap, (lists[i].val, i))

        return dummy.next


# Time complexity : O(NlogN) where N is the total number of nodes.
# Collecting all the values costs O(N) time.
# A stable sorting algorithm costs O(NlogN) time.
# Iterating for creating the linked list costs O(N) time.
# Space complexity : O(N).
# Sorting costs O(N) space (depends on the algorithm you choose).
# Creating a new linked list costs O(N) space.
class BruteForceSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        vals.sort()
        dummy = ListNode(val=-1)
        curr = dummy
        for val in vals:
            curr.next = ListNode(val=val)
            curr = curr.next
        return dummy.next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]

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


class HeapAnotherSolution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for item in lists:
            while item:
                heappush(min_heap, item.val)
                item = item.next
        # print(min_heap)
        dummy = curr = ListNode(-1)
        while min_heap:
            curr.next = ListNode(val=heappop(min_heap))
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    lists = [ListNode(val=1, next=ListNode(val=4, next=ListNode(val=5))),
             ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4))),
             ListNode(val=2, next=ListNode(val=6))]
    HeapSolution().mergeKLists(lists)
