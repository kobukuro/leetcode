# Tags: Math
from typing import List


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def fizz_buzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
