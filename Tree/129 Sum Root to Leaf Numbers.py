# Tree, Depth-First Search, Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root):
        paths = []

        def helper(node, path=None):
            if node:
                if node.left is None and node.right is None:
                    paths.append(path)
                if node.left:
                    helper(node.left, path=path + str(node.left.val))
                if node.right:
                    helper(node.right, path=path + str(node.right.val))

        helper(node=root, path=str(root.val))
        total = 0
        for path in paths:
            total += int(path)
        return total


if __name__ == '__main__':
    root = TreeNode(val=1,
                    left=TreeNode(val=2),
                    right=TreeNode(val=3))
    print(Solution().sumNumbers(root=root))
