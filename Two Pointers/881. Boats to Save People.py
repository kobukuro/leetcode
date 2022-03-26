# Array, Two Pointers, Greedy, Sorting
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
        return ans
