# Tree, Backtracking, Depth-First Search, Binary Tree
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(N^2)
# where N are the number of nodes in a tree.
# In the worst case, we could have a complete binary tree and if that is the case,
# then there would be N/2 leaves. For every leaf, we perform a potential
# O(N) operation of copying over the path nodes to a new list to be added to the final res.
# Hence, the complexity in the worst case could be O(N^2).

# Space Complexity: O(N)
# The only additional space that we use is the path list to keep track of nodes along a branch.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
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

        dfs(root, [], targetSum)
        return res


# https://stackoverflow.com/questions/11177533/whats-the-difference-between-plus-and-append-in-python-for-list-manipulation
class AnotherSolution:

    def pathSum(self, root, targetSum):
        all_paths = []

        def helper(root, path, total):
            if not root.left and not root.right:
                if total == targetSum:
                    all_paths.append(path)
            if root.left:
                helper(root.left, path + [root.left.val], total + root.left.val)
            if root.right:
                helper(root.right, path + [root.right.val], total + root.right.val)

        if root:
            helper(root, [root.val], root.val)
        return all_paths


if __name__ == '__main__':
    root = TreeNode(val=5,
                    left=TreeNode(val=4,
                                  left=TreeNode(val=11,
                                                left=TreeNode(val=7,
                                                              left=None,
                                                              right=None),
                                                right=TreeNode(val=2,
                                                               left=None,
                                                               right=None)),
                                  right=None),
                    right=TreeNode(val=8,
                                   left=TreeNode(val=13,
                                                 left=None,
                                                 right=None),
                                   right=TreeNode(val=4,
                                                  left=TreeNode(val=5,
                                                                left=None,
                                                                right=None),
                                                  right=TreeNode(val=1,
                                                                 left=None,
                                                                 right=None))))
    solution = Solution()
    print(solution.pathSum(root=root, targetSum=22))
