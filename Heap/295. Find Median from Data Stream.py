# Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream
import heapq


# Time complexity : O(log n)
# Space complexity: O(n)
class MedianFinder:

    def __init__(self):
        self.small_heap = []  # max heap
        self.large_heap = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_heap, (-1) * num)
        if len(self.large_heap) > 0 and (-1) * self.small_heap[0] > self.large_heap[0]:
            val = heapq.heappop(self.small_heap) * (-1)
            heapq.heappush(self.large_heap, val)
        if len(self.small_heap) == len(self.large_heap) + 2:
            val = heapq.heappop(self.small_heap) * (-1)
            heapq.heappush(self.large_heap, val)
        if len(self.small_heap) + 2 == len(self.large_heap):
            val = heapq.heappop(self.large_heap)
            heapq.heappush(self.small_heap, val * (-1))

    def findMedian(self) -> float:
        # print(len(self.small_heap), len(self.large_heap), self.small_heap, self.large_heap)
        if len(self.small_heap) == len(self.large_heap):
            return (self.small_heap[0] * (-1) + self.large_heap[0]) / 2
        elif len(self.small_heap) > len(self.large_heap):
            return self.small_heap[0] * (-1)
        else:
            return self.large_heap[0]
