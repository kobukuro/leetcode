# Tags: Tree, DFS
from typing import Optional
from utils.data_structures import TreeNode


class Solution:
    # n: the number of nodes in the tree
    # Time complexity: O(n), since each node in the tree is visited only once.
    # We cannot do better than that, since at the very least we have to visit each node to invert it.

    # Space complexity: O(n).
    # Because of recursion, O(h) function calls will be placed on the stack in the worst case,
    # where h is the height of the tree. Because h∈O(n), the space complexity is O(n).
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root
