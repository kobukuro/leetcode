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
        def dfs(node):
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)
            else:
                return node

        return dfs(root)
