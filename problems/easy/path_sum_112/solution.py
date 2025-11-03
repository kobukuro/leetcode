# Tags: Tree, DFS
from typing import Optional
from utils.data_structures import TreeNode


class Solution:
    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        """
            Time complexity: we visit each node exactly once,
            thus the time complexity is O(N), where N is the number of nodes.

            Space complexity: in the worst case,
            the tree is completely unbalanced,
            e.g. each node has only one child node,
            the recursion call would occur N times (the height of the tree),
            therefore the storage to keep the call stack would be O(N).
        """
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == target_sum:
            return True
        return self.has_path_sum(root.left, target_sum - root.val) or self.has_path_sum(root.right,
                                                                                        target_sum - root.val)
