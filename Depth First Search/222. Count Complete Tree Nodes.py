from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return len(values)

    def countNodesAnotherSolution(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            return 1 + dfs(node.left) + dfs(node.right)

        return dfs(root)
