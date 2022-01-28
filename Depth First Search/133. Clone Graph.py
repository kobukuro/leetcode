# Hash Table, Depth-First Search, Breadth-First Search, Graph
# reference:https://www.youtube.com/watch?v=mQeF6bN8hMk
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mapping = {}

        def dfs(node):
            if node not in mapping:
                copy = Node(val=node.val)
                mapping[node] = copy
                for nei in node.neighbors:
                    copy.neighbors.append(dfs(nei))
            else:
                return mapping[node]
            return copy

        return dfs(node)
