# Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []

        def inorder(root):
            if root:
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)

        inorder(root)
        print(self.arr)
        self.curr_index = -1

    def next(self) -> int:
        self.curr_index += 1
        return self.arr[self.curr_index]

    def hasNext(self) -> bool:
        return self.curr_index + 1 <= len(self.arr) - 1

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
