# Tree, Binary Search Tree, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            # print(root.val)
            return root
        if root.left:
            result = self.searchBST(root.left, val)
            if result:
                return result
        if root.right:
            result = self.searchBST(root.right, val)
            if result:
                return result
        return None
