# Tags: Tree, DFS
from typing import Optional
from utils.data_structures import TreeNode


class Solution:
    # Time complexity: O(N)
    # We visit each node exactly once, thus the time complexity is O(N),
    # where N is the number of nodes.

    # Space complexity: O(N)
    # In the worst case, the tree is completely unbalanced,
    # e.g. each node has only left child node, the recursion call would occur N times
    # (the height of the tree), therefore the storage to keep the call stack would be O(N).
    # But in the best case (the tree is completely balanced), the height of the tree would be log(N).
    # Therefore, the space complexity in this case would be O(log(N)).
    # But big o notation considers worst case, so space complexity is O(N).
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
