# Linked List, Divide and Conquer, Heap(Priority Queue), Merge Sort
# reference:https://www.youtube.com/watch?v=q5a5OiGbT6Q
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


from heapq import heappush, heappop


class HeapSolution:
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
