# Tags: Tree, DFS, Backtracking
from typing import List, Optional

from utils.data_structures import TreeNode


class Solution:
    """
    Time complexity: O(N ^ 2)
    where N are the number of nodes in a tree.
    In the worst case, we could have a complete binary tree and if that is the case,
    then there would be N/2 leaves.
    For every leaf, we perform a potential O(N) operation of copying over the path nodes to a new list
    to be added to the final res.
    Hence, the complexity in the worst case could be O(N^2).

    Space Complexity: O(N)
    The only additional space that we use is the path list to keep track of nodes along a branch.
    """

    def path_sum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, remaining_sum):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right and remaining_sum == node.val:
                res.append(list(path))
            dfs(node.left, path, remaining_sum - node.val)
            dfs(node.right, path, remaining_sum - node.val)
            path.pop()

        dfs(root, [], target_sum)
        return res
