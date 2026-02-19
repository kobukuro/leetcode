# Tags: Graph, DFS, Hash Table
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: 'Node', mapping=None) -> Optional['Node']:
        """
        Time complexity: O(N + M), where N is a number of nodes (vertices) and M is a number of edges.

        Space complexity: O(N). This space is occupied by the visited hash map
        and in addition to that, space would also be occupied by the recursion stack
        since we are adopting a recursive approach here.
        The space occupied by the recursion stack would be equal to O(H)
        where H is the height of the graph. Overall, the space complexity would be O(N).
        """
        if mapping is None:
            mapping = {}
        if node in mapping:
            return mapping[node]
        if node is None:
            return None
        copy = Node(node.val)
        mapping[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(self.clone_graph(nei, mapping))
        return mapping[node]
