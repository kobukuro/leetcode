# Tags: Tree, Binary Tree, Depth-First Search
from utils.data_structures import TreeNode


class Solution:
    def postorder_traversal(self, root: TreeNode | None) -> list[int]:
        """
        Return the postorder traversal (left, right, root) of a binary tree.

        Args:
            root: Root of the binary tree, or None for an empty tree.

        Returns:
            List of node values in postorder.

        Time complexity: O(n)
        - n is the number of nodes in the tree
        - The recursive helper is called once per node (n calls) plus once for
          each missing child (None), at most n + 1 extra calls: 2n + 1 calls
        - Each call does O(1) work: a None check, and for real nodes one
          list.append (amortized O(1), occasional resizing is spread out)
        - Total: O(2n + 1) = O(n); this holds for every tree shape, so best,
          average and worst case are all O(n)

        Space complexity: O(n)
        - h is the height of the tree (log n <= h <= n)
        - Recursion call stack: at most h + 1 frames, so O(h)
          - Balanced tree: O(log n)
          - Skewed tree (every node has one child): O(n)
        - The result list stores n values: O(n)
        - Total: O(n) including the output; auxiliary space excluding the
          output is O(h)
        """
        res = []

        def postorder(node):
            """
            Append values of the subtree rooted at node to res in postorder.

            Args:
                node: Root of the current subtree, or None.

            Returns:
                None; results are accumulated in the enclosing list res.

            Time complexity: O(m)
            - m is the number of nodes in the subtree rooted at node
            - Each node is visited exactly once and does O(1) work
              (one append, two recursive calls); None children return
              immediately in O(1)
            - Total: O(m) for the subtree, O(n) for the whole tree

            Space complexity: O(h)
            - h is the height of the subtree rooted at node
            - Only the call stack is used (at most h + 1 frames); the
              appended values go into res, which is owned by the caller
            - O(log n) for a balanced tree, O(n) for a skewed tree
            """
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res
