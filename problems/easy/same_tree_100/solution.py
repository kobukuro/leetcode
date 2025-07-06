# Tags: Tree, DFS
from typing import Optional
from utils.data_structures import TreeNode


class Solution:
    # Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
    # Space complexity : O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
