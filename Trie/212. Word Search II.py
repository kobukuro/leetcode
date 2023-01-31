# Array, String, Backtracking, Trie, Matrix
from typing import List


class Trie:
    def __init__(self):
        self.links = {}
        self.is_end = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.links:
                curr.links[c] = Trie()
            curr = curr.links[c]
        curr.is_end = True

    def remove_word(self, word):
        curr = self
        node_and_child_key = []
        for c in word:
            node_and_child_key.append((curr, c))
            curr = curr.links[c]
        i = 0
        for parent_node, child_key in reversed(node_and_child_key):
            target_node = parent_node.links[child_key]
            if i == 0:
                target_node.is_end = False
            if len(target_node.links) == 0:
                del parent_node.links[child_key]
            else:
                return
            i += 1


# Time complexity: O(M(4⋅3^(L−1))),
# where M is the number of cells in the board and L is the maximum length of word in words.
# It is tricky to calculate the exact number of steps that a backtracking algorithm would perform.
# We provide a upper bound of steps for the worst scenario for this problem.
# The algorithm loops over all the cells in the board,
# therefore we have M as a factor in the complexity formula.
# It then boils down to the maximum number of steps we would need for each starting cell
# (i.e. 4⋅3^(L−1))
# Assume the maximum length of word is L, starting from a cell,
# initially we would have at most 4 directions to explore.
# Assume each direction is valid (i.e. worst case),
# during the following exploration, we have at most 3 neighbor cells
# (excluding the cell where we come from) to explore.
# As a result, we would traverse at most 4⋅3^(L−1) cells during the backtracking exploration.
# Note that, the above time complexity is estimated under the assumption
# that the Trie data structure would not change once built.
# If we apply the optimization trick to gradually remove the nodes in Trie,
# we could greatly improve the time complexity,
# since the cost of backtracking would reduced to zero
# once we match all the words in the dictionary, i.e. the Trie becomes empty.

# Space Complexity: O(N), where N is the total number of letters in the dictionary.
# The main space consumed by the algorithm is the Trie data structure we build.
# In the worst case where there is no overlapping of prefixes among the words,
# the Trie would have as many nodes as the letters of all words.
# And optionally, one might keep a copy of words in the Trie as well. As a result,
# we might need 2N space for the Trie.
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for word in words:
            root.add_word(word)
        ROWS, COLS = len(board), len(board[0])
        res, visited = [], set()

        def dfs(r, c, node, word):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited or
                    board[r][c] not in node.links):
                return
            visited.add((r, c))
            node = node.links[board[r][c]]
            word += board[r][c]
            if node.is_end:
                res.append(word)
                root.remove_word(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return res
