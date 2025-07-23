# Tags: Tree, BFS
from collections import deque
from typing import List

from utils.data_structures import Node


class Solution:
    # Time complexity : O(n), where n is the number of nodes.
    # Each node is getting added to the queue, removed from the queue, and added to the result exactly once.

    # Space complexity : O(n).
    # We are using a queue to keep track of nodes we still need to visit the children of.
    # At most, the queue will have 2 layers of the tree on it at any given time.
    # In the worst case, this is all the nodes.
    # In the best case, it is just 1 node (if we have a tree that is equivalent to a linked list).
    # The average case is difficult to calculate without knowing something of the trees we can expect to see,
    # but in balanced trees, half or more of the nodes are often in the lowest 2 layers.
    # So we should go with the worst case of O(n), and know that the average case is probably similar.
    def level_order(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    for child in node.children:
                        queue.append(child)
            res.append(level)
        return res
