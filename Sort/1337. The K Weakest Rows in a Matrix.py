# Array, Binary Search, Sorting, Heap(Priority Queue), Matrix
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_list = []
        for i in range(len(mat)):
            num_list.append((i, mat[i].count(1)))
        num_list = sorted(num_list, key=lambda x: x[1])
        print(num_list)
        ans = []
        for i in range(k):
            ans.append(num_list[i][0])
        return ans
