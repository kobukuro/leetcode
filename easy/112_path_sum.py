# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        all_match_paths = []

        def helper(root, path, total):
            if not root.left and not root.right:
                if total == targetSum:
                    all_match_paths.append(path)
            if root.left:
                helper(root.left, path + [root.left.val], total=total + root.left.val)
            if root.right:
                helper(root.right, path + [root.right.val], total=total + root.right.val)

        if root:
            helper(root=root, path=[root.val], total=root.val)
        if all_match_paths:
            return True
        else:
            return False


if __name__ == '__main__':
    root = TreeNode(val=5,
                    left=TreeNode(val=4,
                                  left=TreeNode(val=11,
                                                left=TreeNode(val=7,
                                                              left=None,
                                                              right=None),
                                                right=TreeNode(val=2,
                                                               left=None,
                                                               right=None)),
                                  right=None),
                    right=TreeNode(val=8,
                                   left=TreeNode(val=13,
                                                 left=None,
                                                 right=None),
                                   right=TreeNode(val=4,
                                                  left=None,
                                                  right=TreeNode(val=1,
                                                                 left=None,
                                                                 right=None))))
    solution = Solution()
    print(solution.hasPathSum(root=root, targetSum=22))
