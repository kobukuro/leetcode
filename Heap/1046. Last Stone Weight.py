# Array, Heap(Priority Queue)
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        heap = []
        heapq.heapify(heap)
        for i in range(len(stones)):
            heapq.heappush(heap, (-1) * stones[i])

        while len(heap) > 1:
            item1 = heapq.heappop(heap)
            item2 = heapq.heappop(heap)
            print(item1, item2)
            if item1 != item2:
                heapq.heappush(heap, (item1 - item2))
            print(heap)
        ans = 0
        for ele in heap:
            ans += (-1) * ele
        return ans
