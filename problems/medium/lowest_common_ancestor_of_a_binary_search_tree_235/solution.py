# Tags: Tree, DFS, Binary Search Tree
from utils.data_structures import TreeNode


class Solution:
    # Time complexity: O(N),
    # where N is the number of nodes in the BST.
    # In the worst case we might be visiting all the nodes of the BST.

    # Space complexity: O(N).
    # This is because the maximum amount of space
    # utilized by the recursion stack would be N
    # since the height of a skewed BST could be N.
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowest_common_ancestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowest_common_ancestor(root.right, p, q)
        return root
