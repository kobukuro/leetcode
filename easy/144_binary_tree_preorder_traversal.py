# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive version
# class Solution:
#
#     def preorderTraversal(self, root):
#         # root -> left -> right
#         def preorder(node):
#             if node:
#                 ans.append(node.val)
#                 preorder(node.left)
#                 preorder(node.right)
#
#         ans = []
#         preorder(root)
#         return ans

# iterative  version
class Solution:
    def preorderTraversal(self, root):
        stack = [root]
        result = []
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result


if __name__ == '__main__':
    root = TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3)))
    print(Solution().preorderTraversal(root=root))
