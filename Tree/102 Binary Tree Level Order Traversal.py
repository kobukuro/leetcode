# Tree, Breadth-First Search, Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity : O(N) since each node is processed exactly once.
    # Space complexity: The space complexity for BFS is O(w) where w is the maximum width of the tree.
    # Due to the nature of BFS, at any given moment, the queue holds no more than two levels of nodes.
    # In the worst case, a level in a full binary tree contains at most half of the total nodes
    # (i.e. N/2), i.e. this is also the level where the leaf nodes reside.
    # Hence, the overall space complexity of the algorithm is O(N). (/2 could be ignored)
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
