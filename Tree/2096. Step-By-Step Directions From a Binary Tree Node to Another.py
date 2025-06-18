# String, Tree, Depth-First Search, Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca = self._find_lca(root, startValue, destValue)
        path_to_start = []
        path_to_dest = []

        self._find_path(lca, startValue, path_to_start)
        self._find_path(lca, destValue, path_to_dest)

        res = []
        res.extend(['U' for _ in range(len(path_to_start))])
        res.extend(path_to_dest)

        return ''.join(res)

    def _find_lca(self, root, start_val, dest_val):
        if root is None:
            return None
        if root.val == start_val or root.val == dest_val:
            return root
        l = self._find_lca(root.left, start_val, dest_val)
        r = self._find_lca(root.right, start_val, dest_val)
        if l is None:
            return r
        if r is None:
            return l
        return root

    def _find_path(self, root, target_val, path):
        if root is None:
            return False
        if root.val == target_val:
            return True
        path.append('L')
        if self._find_path(root.left, target_val, path):
            return path
        path.pop()

        path.append('R')
        if self._find_path(root.right, target_val, path):
            return path
        path.pop()

        return False
