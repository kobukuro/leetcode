# Tags: Tree, DFS
from typing import Optional
from utils.data_structures import TreeNode


class Solution:
    def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
            Time complexity: O(H), where H is a tree height.
            That results in O(logN) in the average case, and O(N) in the worst case.

            Space complexity: O(H) to keep the recursion stack,
            i.e. O(logN) in the average case, and O(N) in the worst case.
        """
        if root is None or root.val == val:
            return root
        return self.search_bst(root.left, val) if val < root.val else self.search_bst(root.right, val)
