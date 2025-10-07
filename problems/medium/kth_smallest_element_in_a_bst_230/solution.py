# Tags: Tree, Binary Search Tree, DFS
from typing import Optional

from utils.data_structures import TreeNode


class Solution:
    """
        Time complexity : O(N) to build a traversal.
        Space complexity : O(N) to keep an inorder traversal.
    """

    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return values[k - 1]
