# Stack, Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []

        def inorder(root):
            if root:
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)

        inorder(root)
        res = TreeNode(val=arr[0])
        curr = res
        for i in range(1, len(arr)):
            nxt = TreeNode(val=arr[i])
            curr.right = nxt
            curr = nxt
        return res
