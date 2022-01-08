# Tree, Backtracking, Depth-First Search, Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root, targetSum):
        all_paths = []

        def helper(root, path, total):
            if not root.left and not root.right:
                if total == targetSum:
                    all_paths.append(path)
            if root.left:
                helper(root.left, path + [root.left.val], total + root.left.val)
            if root.right:
                helper(root.right, path + [root.right.val], total + root.right.val)
        if root:
            helper(root, [root.val], root.val)
        return all_paths


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
                                                  left=TreeNode(val=5,
                                                                left=None,
                                                                right=None),
                                                  right=TreeNode(val=1,
                                                                 left=None,
                                                                 right=None))))
    solution = Solution()
    print(solution.pathSum(root=root, targetSum=22))
