# Tags: Graph, DFS, Hash Table
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: 'Node', mapping=None) -> Optional['Node']:
        """
        Time complexity: O(N + M), where N is the number of nodes (vertices) and M is the number of edges.

        Space complexity: O(N). This space is occupied by the visited hash map,
        and in addition to that, space is also occupied by the recursion stack
        since we are adopting a recursive approach here.
        The recursion stack depth can be up to O(N) in the worst case (for example,
        when the graph forms a simple chain). Overall, the space complexity is O(N).
        """
        if node is None:
            return None
        if mapping is None:
            mapping = {}
        if node in mapping:
            return mapping[node]
        copy = Node(node.val)
        mapping[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(self.clone_graph(nei, mapping))
        return mapping[node]
