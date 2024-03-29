# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time Complexity: O(N),
# where N is the number of nodes in the BST.
# In the worst case we might be visiting all the nodes of the BST.
#
# Space Complexity: O(N).
# This is because the maximum amount of space
# utilized by the recursion stack would be N
# since the height of a skewed BST could be N.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val < q.val:
            return root
        if p.val > root.val > q.val:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        if root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)
