# Tags: Tree, Binary Tree, Depth-First Search
from utils.data_structures import TreeNode


class Solution:
    def preorder_traversal(self, root: TreeNode | None) -> list[int]:
        """
        Return the preorder (node, left, right) traversal of a binary tree.

        Args:
            root: Root of the binary tree, or None for an empty tree.

        Returns:
            List of node values in preorder order.

        Time complexity: O(n)
        - n is the number of nodes in the tree, h is the height of the tree
          (log n <= h <= n for a binary tree, h = n for a skewed tree)
        - preorder() is called once for every node: n calls
        - It is also called once for every missing child (None); a binary
          tree with n nodes has n + 1 such null links: n + 1 calls
        - Each call does O(1) work: a None check and, for real nodes, one
          amortized O(1) list append
        - Total: (n + n + 1) calls * O(1) = O(n)
        - Best, average and worst case are all O(n) because every node must
          be visited regardless of the tree shape

        Space complexity: O(n)
        - res stores one value per node: O(n); this is the output
        - Recursion call stack depth equals the tree height h: O(h), which is
          O(log n) for a balanced tree and O(n) for a skewed tree
        - Total: O(n) including the output; auxiliary space excluding the
          output is O(h)
        """
        res = []

        def preorder(node):
            """
            Append the values of the subtree rooted at node in preorder.

            Args:
                node: Current subtree root, or None for an empty subtree.

            Time complexity: O(m)
            - m is the number of nodes in the subtree rooted at node
            - Each node is visited once and does O(1) work (one append);
              each None child returns immediately in O(1)

            Space complexity: O(h')
            - h' is the height of the subtree rooted at node
            - Only the recursion call stack is used; res is shared with the
              enclosing function and accounted for there
            """
            if node is None:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return res
