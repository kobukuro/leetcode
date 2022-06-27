# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []

        def in_order(root):
            if root:
                in_order(root.left)
                arr.append(root.val)
                in_order(root.right)

        in_order(root)
        res = 0
        for ele in arr:
            if ele >= low and ele <= high:
                res += ele
        return res
