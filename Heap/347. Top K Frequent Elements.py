# Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
from collections import defaultdict
import heapq
from typing import List


# Time complexity : O(N log k)
# Space complexity : O(N)
class HeapSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # region Time: O(N), Space:O(N)
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # endregion
        ans = []
        # region Time: O(N log k), Space:O(k)
        for key, value in freq.items():
            heapq.heappush(ans, [value, key])
            if len(ans) > k:
                heapq.heappop(ans)
        # endregion
        return [key for value, key in ans]


# Time complexity : O(N log N)
# Space complexity : O(N)
class BruteForceSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        ans = []
        for key, value in sorted(count.items(), key=lambda item: item[1], reverse=True):
            ans.append(key)
            k -= 1
            if k == 0:
                break
        return ans
