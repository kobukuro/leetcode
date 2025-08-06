# Tags: Math
from typing import List


class Solution:
    # Time complexity: O(1)
    # Space complexity: O(1)
    def convert_temperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]
