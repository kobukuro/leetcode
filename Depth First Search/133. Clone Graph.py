# Hash Table, Depth-First Search, Breadth-First Search, Graph
# reference:https://www.youtube.com/watch?v=mQeF6bN8hMk

# Time Complexity: O(N + M), where N is a number of nodes (vertices) and M is a number of edges.
# Space Complexity: O(N). This space is occupied by the visited hash map
# and in addition to that, space would also be occupied by the recursion stack
# since we are adopting a recursive approach here.
# The space occupied by the recursion stack would be equal to O(H)
# where H is the height of the graph. Overall, the space complexity would be O(N).

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
