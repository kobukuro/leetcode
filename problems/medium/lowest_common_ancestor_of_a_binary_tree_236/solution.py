# Tags: Tree, DFS
from utils.data_structures import TreeNode


class Solution:
    """
        Time complexity: O(N),
        where N is the number of nodes in the binary tree.
        In the worst case we might be visiting all the nodes of the binary tree.

        Space complexity: O(N).
        This is because the maximum amount of space utilized by the recursion stack would be N
        since the height of a skewed binary tree could be N.
    """

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == p or root == q or not root:
            return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
