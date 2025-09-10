# Tags: String, Hash Set


class Solution:
    """
    Time complexity: O(J + S)
    Breakdown:
    -   Set creation: set(jewels) creates a set from the jewels string
        -   This operation iterates through all J characters in the jewels string
        -   Each character insertion into the set takes O(1) average time
        -   Total: O(J)
    -   Main loop: Iterates through each character in the stones string of length S
        -   Each in operation on the set takes O(1) average time for lookup
        -   Total: O(S)
    -   Overall: O(J) + O(S) = O(J + S)
    Where J is the length of the jewels string and S is the length of the stones string.

    Space complexity: O(J)
    Breakdown:
    -   Set storage: The jewel_types set stores at most J unique characters from the jewels string
        -   In the worst case, all characters in jewels are unique, requiring O(J) space
    -   Other variables: res uses O(1) constant space
    -   Overall: O(J)
    """

    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        res = 0
        jewel_types = set(jewels)
        for stone in stones:
            if stone in jewel_types:
                res += 1
        return res
