# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        ans = []

        def helper(root, path):
            if not root.left and not root.right:
                ans.append(path)
            if root.left:
                helper(root.left, path + '->' + str(root.left.val))
            if root.right:
                helper(root.right, path + '->' + str(root.right.val))

        helper(root=root, path=str(root.val))

        return ans


if __name__ == '__main__':
    root = TreeNode(val=1,
                    left=TreeNode(val=2,
                                  left=None,
                                  right=TreeNode(val=5,
                                                 left=None,
                                                 right=None)),
                    right=TreeNode(val=3,
                                   left=None,
                                   right=None))
    solution = Solution()
    print(solution.binaryTreePaths(root=root))
