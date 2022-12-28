# Dynamic Programming, Tree, Depth-First Search, Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Let n be the number of nodes in the tree.
# Time complexity: O(n)
# Each node in the tree is visited only once.
# During a visit, we perform constant time operations,
# including two recursive calls and calculating the max path sum for the current node.
# So the time complexity is O(n).

# Space complexity: O(n)O(n)
# We don't use any auxiliary data structure,
# but the recursive call stack can go as deep as the tree's height.
# In the worst case, the height of tree is n. Therefore, the space complexity is O(n).
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-float('inf')]

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(0, left)
            right = max(0, right)
            res[0] = max(res[0], node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return res[0]
