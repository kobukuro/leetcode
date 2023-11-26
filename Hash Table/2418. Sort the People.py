from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapping = {}
        for i in range(len(heights)):
            mapping[heights[i]] = i
        res = sorted(heights, reverse=True)
        for i in range(len(res)):
            res[i] = names[mapping[res[i]]]
        return res
