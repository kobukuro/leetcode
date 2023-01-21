# Tree, Depth-First Search, Breadth-First Search, Binary Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preOrderTraversal(self, root):
        ans = []

        def preorder(root):
            if root:
                ans.append(root.val)
                preorder(root.left)
                preorder(root.right)
            else:
                ans.append(None)

        preorder(root)
        return ans

    def isSameTree(self, p, q):
        return self.preOrderTraversal(p) == self.preOrderTraversal(q)


class AnotherSolution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    p = TreeNode(val=1,
                 left=TreeNode(val=1))
    q = TreeNode(val=1,
                 right=TreeNode(val=1))
    solution = Solution()
    print(solution.isSameTree(p=p, q=q))
