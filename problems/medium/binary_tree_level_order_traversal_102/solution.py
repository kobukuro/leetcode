# Tags: Tree, BFS
from typing import List, Optional
from collections import deque
from utils.data_structures import TreeNode


class Solution:
    # Time complexity : O(N) since each node is processed exactly once.
    # Space complexity: O(N)
    # The space complexity for BFS is O(w) where w is the maximum width of the tree.
    # Due to the nature of BFS, at any given moment, the queue holds no more than two levels of nodes.
    # In the worst case, a level in a full binary tree contains at most half of the total nodes
    # (i.e. N/2), i.e. this is also the level where the leaf nodes reside.
    # Hence, the overall space complexity of the algorithm is O(N). (/2 could be ignored)
    def level_order(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])  # Using deque for efficient pop from the left
        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level)
        return ans
