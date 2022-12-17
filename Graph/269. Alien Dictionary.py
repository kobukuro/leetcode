# Array, String, Depth-First Search, Breadth-First Search, Graph, Topological Sort
from collections import defaultdict, deque
from typing import List


# Let C be the total length of all the words in the input list, added together.
# Let U be the total number of unique letters in the alien alphabet.
# This is limited to 26 in the question description.
# Time complexity : O(C).
# Space complexity : O(1).
# For the question we're given, where U is a constant fixed at a maximum of 26,
# the space complexity is simply O(1)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ''
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        if len(output) < len(in_degree):
            return ''
        return ''.join(output)


if __name__ == '__main__':
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    # words = ["z", "x", "z"]
    print(Solution().alienOrder(words=words))
