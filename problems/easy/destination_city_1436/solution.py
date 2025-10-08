# Tags: Array, Hash Set
from typing import List


class Solution:
    """
    Given n as the length of paths,

    Time complexity: O(n)
    We first iterate over paths to populate has_outgoing, this costs O(n).
    Next, we iterate over paths again to find the answer,
    checking at each step whether candidate is in the hash set, which takes O(1).
    Thus, the iteration costs O(n).

    Space complexity: O(n)
    has_outgoing will grow to a size of O(n).
    """

    def dest_city(self, paths: List[List[str]]) -> str:
        has_outgoing = set()
        for start, _ in paths:
            has_outgoing.add(start)
        for _, end in paths:
            if end not in has_outgoing:
                return end
        return ""
