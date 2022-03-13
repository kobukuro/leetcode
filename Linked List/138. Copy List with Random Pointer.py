# Hash Table, Linked List
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        if head.next is None:
            if head.random is None:
                return Node(x=head.val)
            else:
                new_node = Node(x=head.val)
                new_node.random = new_node
                return new_node

        def dfs(node, mapping=None):
            if mapping is None:
                mapping = {}
            if node in mapping:
                return mapping[node]
            mapping[node] = Node(x=node.val)
            curr = node
            while curr is not None:
                if curr.next is not None:
                    if curr.next not in mapping:
                        mapping[curr.next] = Node(x=curr.next.val)
                    mapping[curr].next = mapping[curr.next]
                if curr.random is not None:
                    if curr.random not in mapping:
                        mapping[curr.random] = Node(x=curr.random.val)
                    mapping[curr].random = mapping[curr.random]
                curr = curr.next
            return mapping[node]

        return dfs(head)
