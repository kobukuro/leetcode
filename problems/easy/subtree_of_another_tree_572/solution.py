# Tags: Tree, DFS
from typing import Optional
from utils.data_structures import TreeNode


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

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
    def is_subtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if sub_root is None:
            return True
        if root is None:
            return False
        if self.is_same_tree(root, sub_root):
            return True
        return self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)
