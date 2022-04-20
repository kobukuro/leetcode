# Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nums = []

        def inorder(root):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)

        def swap(nums):
            x = y = None
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x is None:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(root, count):
            if root:
                if root.val == x:
                    root.val = y
                    count -= 1
                elif root.val == y:
                    root.val = x
                    count -= 1
                if count == 0:
                    return
                recover(root.left, count)
                recover(root.right, count)

        inorder(root)
        x, y = swap(nums)
        print(nums)
        print(x, y)
        recover(root, 2)
