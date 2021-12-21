# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        paths = []

        def helper(node, path):
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                helper(node.left, path + [node.left.val])
            if node.right:
                helper(node.right, path + [node.right.val])

        helper(root, [root.val])
        ans = len(paths[0])
        for path in paths:
            if len(path) < ans:
                ans = len(path)
        return ans


if __name__ == '__main__':
    root = TreeNode(val=3,
                    left=TreeNode(val=9),
                    right=TreeNode(val=20,
                                   left=TreeNode(val=15),
                                   right=TreeNode(val=7)))
    print(Solution().minDepth(root=root))
