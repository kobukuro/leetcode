# Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans


if __name__ == '__main__':
    root = TreeNode(val=3,
                    left=TreeNode(val=9),
                    right=TreeNode(val=20,
                                   left=TreeNode(val=15),
                                   right=TreeNode(val=7)))
    solution = Solution()
    print(solution.levelOrder(root=root))
