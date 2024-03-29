# Tree, Stack, Depth-First Search, Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive version
# class Solution:
#     # left -> root -> right
#     def inorderTraversal(self, root):
#         res = []
#
#         def inorder(node):
#             if not node:
#                 return
#             inorder(node.left)
#             res.append(node.val)
#             inorder(node.right)
#
#         inorder(root)
#         return res


# iterative  version
# class Solution:
#     def inorderTraversal(self, root):
#         stack = []
#         result = []
#         while root or stack != []:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             result.append(root.val)
#             root = root.right
#         return result


# iterative  version 2
class Solution:
    def inorderTraversal(self, root):
        res = []

        stack = [(root, False)]

        while stack:

            node, visited = stack.pop()

            if node:
                if visited:
                    res.append(node.val)


                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        return res


if __name__ == '__main__':
    root = TreeNode(val=1,
                    left=None,
                    right=TreeNode(val=2,
                                   left=TreeNode(val=3,
                                                 left=None,
                                                 right=None),
                                   right=None))
    solution = Solution()
    print(solution.inorderTraversal(root=root))
