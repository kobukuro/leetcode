from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i][0], points[i][1]
            target_x, target_y = points[i + 1][0], points[i + 1][1]
            if curr_x != target_x and curr_y != target_y:
                if abs(target_x - curr_x) <= abs(target_y - curr_y):
                    diff = target_x - curr_x
                    curr_x = target_x
                    if abs(target_y - (curr_y + diff)) <= abs(target_y - (curr_y - diff)):
                        curr_y = curr_y + diff
                    else:
                        curr_y = curr_y - diff
                    res += abs(diff)
                else:
                    diff = target_y - curr_y
                    if abs(target_x - (curr_x + diff)) <= abs(target_x - (curr_x - diff)):
                        curr_x = curr_x + diff
                    else:
                        curr_x = curr_x - diff
                    curr_y = target_y
                    res += abs(diff)
            res += max(abs(target_x - curr_x), abs(target_y - curr_y))
        return res
