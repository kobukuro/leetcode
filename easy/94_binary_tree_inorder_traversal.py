# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive version
# class Solution:
#     # left -> root -> right
#     def inorderTraversal(self, root):
#         ans = []
#
#         def helper(root):
#             if root:
#                 helper(root.left)
#                 ans.append(root.val)
#                 helper(root.right)
#
#         helper(root)
#         return ans

# iterative  version
class Solution:
    def inorderTraversal(self, root):
        stack = []
        result = []
        while root or stack != []:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result


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
