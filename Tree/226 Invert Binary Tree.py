# Tree, Depth-First Search, Breadth-First Search, Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        def helper(node):
            node.left, node.right = node.right, node.left
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(node=root)
        return root


if __name__ == '__main__':
    root = TreeNode(val=4,
                    left=TreeNode(val=2,
                                  left=TreeNode(val=1),
                                  right=TreeNode(val=3)),
                    right=TreeNode(val=7,
                                   left=TreeNode(val=6),
                                   right=TreeNode(val=9)))
    print(Solution().invertTree(root=root))
