# Linked List, Hash Table, Two Pointers
# reference:https://www.youtube.com/watch?v=gBTe7lFR3vc
# fast, slow pointers solution
class SolutionFastSlowPointers:
    def hasCycle(self, head) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# hashmap solution
class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        visited = {}
        node = head
        while node.next is not None:
            if node not in visited:
                visited[node] = True
            else:
                return True
            node = node.next
        return False
