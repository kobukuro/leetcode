# String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time complexity : in both serialization and deserialization functions,
# we visit each node exactly once, thus the time complexity is O(N),
# where N is the number of nodes, i.e. the size of tree.
# Space complexity : in both serialization and deserialization functions,
# we keep the entire tree, either at the beginning or at the end,
# therefore, the space complexity is O(N).
class Codec:

    def serialize(self, root):
        res = []

        def preorder(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ','.join(res)

    def deserialize(self, data):
        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
