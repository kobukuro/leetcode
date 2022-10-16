# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned:
            if cloned.val == target.val:
                return cloned
            value = self.getTargetCopy(original, cloned.left, target)
            if value:
                return value
            return self.getTargetCopy(original, cloned.right, target)
