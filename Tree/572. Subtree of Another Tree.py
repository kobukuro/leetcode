# Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# N is the number of nodes in the tree rooted at the root
# M is the number of nodes in the tree rooted at subRoot
# Time complexity: O(MN).
# For every N node in the tree,
# we check if the tree rooted at node is identical to subRoot.
# This check takes O(M) time, where M is the number of nodes in subRoot.
# Hence, the overall time complexity is O(MN).
# Space complexity: O(M+N).
# There will be at most N recursive call to isSubtree.
# Now, each of these calls will have M recursive calls to is_same_tree.
# Before calling is_same_tree, our call stack has at most O(N) elements
# and might increase to O(N+M) during the call.
# After calling is_same_tree,
# it will be back to at most O(N) since all elements made by is_same_tree are popped out.
# Hence, the maximum number of elements in the call stack will be M+N.
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.is_same_tree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def is_same_tree(self, p, q):
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val != q.val:
            return False
        return (self.is_same_tree(p.left, q.left) and
                self.is_same_tree(p.right, q.right))
