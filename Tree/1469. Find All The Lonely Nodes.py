# Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        parents = {}

        def dfs(node, parent=None):
            if node:
                if parent not in parents:
                    parents[parent] = [node.val]
                else:
                    parents[parent].append(node.val)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        # print(parents)
        res = []
        for key, value in parents.items():
            if key is not None and len(value) == 1:
                res.append(value[0])
        return res
