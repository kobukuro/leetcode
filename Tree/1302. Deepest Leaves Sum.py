# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = {}

        def dfs(node, level=0):
            if node:
                if level not in levels:
                    levels[level] = node.val
                else:
                    levels[level] += node.val
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root)
        return levels[max(levels, key=int)]
