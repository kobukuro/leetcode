# Array, Backtracking
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(sum, numbers, number, path):
            # print(f'{sum}-{number}={sum-number}')
            sum -= number
            if sum == 0:
                path.sort()
                if path not in res:
                    res.append(path)
            if sum < 0:
                return
            for num in numbers:
                dfs(sum, numbers, num, path=path + [num])

        for number in candidates:
            dfs(target, candidates, number, path=[number])
        return res
