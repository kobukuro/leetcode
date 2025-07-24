# Tags: Linked List, Two Pointers, Hash Table


class Solution:
    # Fast and slow pointers solution
    # Time complexity: O(n). Let us denote n as the total number of nodes in the linked list.
    # To analyze its time complexity, we consider the following two cases separately.

    # List has no cycle:
    # The fast pointer reaches the end first and the run time depends on the list's length,
    # which is O(n).

    # List has a cycle:
    # We break down the movement of the slow pointer into two steps, the non-cyclic part and the cyclic part:

    # The slow pointer takes "non-cyclic length" steps to enter the cycle.
    # At this point, the fast pointer has already reached the cycle.
    # Number of iterations = non-cyclic length = N

    # Both pointers are now in the cycle.
    # Consider two runners running in a cycle -
    # the fast runner moves 2 steps while the slow runner moves 1 steps at a time.
    # Since the speed difference is 1,
    # it takes (distance between the 2 runners) / (difference of speed)
    # loops for the fast runner to catch up with the slow runner.
    # As the distance is at most "cyclic length K" and the speed difference is 1,
    # we conclude that Number of iterations = almost "cyclic length K".

    # Therefore, the worst case time complexity is O(N+K), which is O(n).

    # Space complexity: O(1). We only use two pointers (slow and fast) so the space complexity is O(1).
    def has_cycle_two_pointers(self, head) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    # Hash set solution
    # Let n be the total number of nodes in the linked list.

    # Time complexity: O(n). We visit each of the n elements in the list at most once.
    # Adding a node to the hash set costs only O(1) time.

    # Space complexity: O(n).
    # The space depends on the number of elements added to the hash set,
    # which contains at most n elements.
    def has_cycle_hash_set(self, head) -> bool:
        if not head:
            return False
        visited = set()
        node = head
        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
