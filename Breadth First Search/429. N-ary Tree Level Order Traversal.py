# Tree, Breadth-First Search
from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(temp)
        return res
