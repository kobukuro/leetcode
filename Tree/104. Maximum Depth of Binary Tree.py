# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):
            if node.left is None and node.right is None:
                return level
            left_height = dfs(node.left, level + 1) if node.left else level
            right_height = dfs(node.right, level + 1) if node.right else level
            return max(left_height, right_height)

        return dfs(root, 1) if root else 0
