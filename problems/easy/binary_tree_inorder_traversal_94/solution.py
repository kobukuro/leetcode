# Tags: Tree, Binary Tree, Depth-First Search
from utils.data_structures import TreeNode


class Solution:
    def inorder_traversal(self, root: TreeNode | None) -> list[int]:
        """
        Return the inorder (left, node, right) traversal of a binary tree.

        Args:
            root: Root of the binary tree, or None for an empty tree.

        Returns:
            List of node values in inorder order.

        Time complexity: O(n)
        - n is the number of nodes in the tree, h is the height of the tree
          (log n <= h <= n for a binary tree, h = n for a skewed tree)
        - inorder() is called once for every node: n calls
        - It is also called once for every missing child (None); a binary
          tree with n nodes has n + 1 such null links: n + 1 calls
        - Each call does O(1) work: a None check and, for real nodes, one
          amortized O(1) list append
        - Total: (n + n + 1) calls * O(1) = O(n)
        - Best, average and worst case are all O(n) because every node must
          be visited regardless of the tree shape

        Space complexity: O(n)
        - res stores one value per node: O(n); this is the output
        - Recursion call stack depth equals the tree height h: O(h)
          (balanced tree: O(log n), skewed tree: O(n))
        - Auxiliary space excluding the output: O(h)
        - Total including the output: O(n) + O(h) = O(n), since h <= n
        """
        res = []

        def inorder(node):
            """
            Append the values of the subtree rooted at node to res in inorder.

            Args:
                node: Root of the current subtree, or None.

            Returns:
                None. Results are accumulated in the enclosing res list.

            Time complexity: O(m)
            - m is the number of nodes in the subtree rooted at node
            - Each node in the subtree is entered once, plus one call per
              null child (m + 1 of them), each with O(1) work
            - Total: O(m) for the subtree, O(n) when called on the root

            Space complexity: O(h')
            - h' is the height of the subtree rooted at node
            - Only the recursion call stack is used (one frame per level);
              res is shared with the enclosing function and not counted here
            - Balanced: O(log m); skewed: O(m)
            """
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res
