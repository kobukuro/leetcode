# Array, Greedy, Heap(Priority Queue), Ordered Set
# reference:https://www.youtube.com/watch?v=l_o4fp6BHYY
# reference:https://www.geeksforgeeks.org/max-heap-in-python/
from typing import List
import heapq
import sys


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        # print(type(nums))
        # print(heap)
        # 先將所有奇數*2, 這樣接下來操作就只有除法了
        low = sys.maxsize
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i] *= 2
            heapq.heappush(heap, (-1) * nums[i])
            low = min(low, nums[i])
        # for i in heap:
        #     print(-1 * i, end=' ')
        # print("Head value of heap : " + str(-1 * heap[0]))
        # print(low)
        # 持續將最大值/2, 直到最大值為奇數時停止, 但ans要回傳較小的值
        ans = (-1) * heap[0] - low
        while (-1) * heap[0] % 2 == 0:
            item = heapq.heappop(heap)
            heapq.heappush(heap, item // 2)
            low = min(low, (-1) * item // 2)
            ans = min(ans, (-1) * heap[0] - low)
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().minimumDeviation(nums=nums))
    nums = [4, 1, 5, 20, 3]
    print(Solution().minimumDeviation(nums=nums))
    nums = [3, 5]
    print(Solution().minimumDeviation(nums=nums))
