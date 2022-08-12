# Tree, Depth-First Search, Binary Search Tree, Binary Tree
from typing import Optional
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity : O(N)
# Space complexity : O(N)
class ConciseSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def inorder(node):
            if node:
                if not inorder(node.left):
                    return False
                if node.val <= self.prev:
                    return False
                self.prev = node.val
                if not inorder(node.right):
                    return False
            return True

        self.prev = -math.inf
        return inorder(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(node):
            if node.left:
                inorder(node.left)
            arr.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        # print(arr)
        prev = None
        for i in range(len(arr)):
            if prev is None:
                prev = arr[i]
            else:
                if arr[i] <= prev:
                    return False
                else:
                    prev = arr[i]
        return True


class AnotherSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inorder(node):
            if node.left:
                if not inorder(node.left):
                    return False
            if arr:
                if node.val <= arr[-1]:
                    return False
                arr.append(node.val)
            else:
                arr.append(node.val)
            if node.right:
                if not inorder(node.right):
                    return False
            return True

        return inorder(root)
