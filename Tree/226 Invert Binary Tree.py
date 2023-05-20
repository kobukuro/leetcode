# Tree, Depth-First Search, Breadth-First Search, Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# n:the number of nodes in the tree
# Time:O(n)
# Space:O(n)
class Solution:
    def invertTree(self, root):
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
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
