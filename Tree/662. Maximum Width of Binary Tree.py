# Tree, DFS, BFS, Binary Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 給編號:parent:1, left為parent*2, right為parent*2+1
# 寬度為每一層max(num)-min(num)+1
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 1
        level_recs = {}

        def dfs(node, level, num):
            if level not in level_recs:
                level_recs[level] = [num]
            else:
                level_recs[level].append(num)
            if node.left:
                dfs(node.left, level + 1, num * 2)
            if node.right:
                dfs(node.right, level + 1, num * 2 + 1)

        dfs(root, 1, 1)
        # print(level_recs)
        res = 1
        for key, value in level_recs.items():
            # print(value)
            res = max(res, max(value) - min(value) + 1)
            # print(key, res)
        return res


if __name__ == '__main__':
    # root = TreeNode(val=1,
    #                 left=TreeNode(val=3,
    #                               left=TreeNode(val=5),
    #                               right=TreeNode(val=3)),
    #                 right=TreeNode(val=2,
    #                                right=TreeNode(val=9)))
    root = TreeNode(val=1,
                    left=TreeNode(val=3,
                                  left=TreeNode(val=5)),
                    right=TreeNode(val=2))
    print(Solution().widthOfBinaryTree(root=root))
