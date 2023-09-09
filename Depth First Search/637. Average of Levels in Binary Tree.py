from typing import Optional, List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        mapping = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            mapping[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        res = []
        for key, values in mapping.items():
            res.append(sum(values) / len(values))
        return res
