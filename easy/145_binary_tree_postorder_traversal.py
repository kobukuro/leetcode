# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive solution
# class Solution:
#     def postorderTraversal(self, root):
#         ans = []
#
#         def postorder(root):
#             if root.left:
#                 postorder(root.left)
#             if root.right:
#                 postorder(root.right)
#             ans.append(root.val)
#
#         if root:
#             postorder(root)
#         return ans


# iterative  version
class Solution:
    def postorderTraversal(self, root):
        pass


if __name__ == '__main__':
    root = TreeNode(val=1,
                    left=None,
                    right=TreeNode(val=2,
                                   left=TreeNode(val=3,
                                                 left=None,
                                                 right=None),
                                   right=None))
    solution = Solution()
    print(solution.postorderTraversal(root=root))
