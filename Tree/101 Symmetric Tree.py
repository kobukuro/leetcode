# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        queue = [(root.left, root.right)]
        while queue:
            left, right = queue.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True


if __name__ == '__main__':
    root = TreeNode(val=1,
                    left=TreeNode(val=2,
                                  left=TreeNode(val=3),
                                  right=TreeNode(val=4)),
                    right=TreeNode(val=2,
                                   left=TreeNode(val=4),
                                   right=TreeNode(val=3)))
    print(Solution().isSymmetric(root=root))
