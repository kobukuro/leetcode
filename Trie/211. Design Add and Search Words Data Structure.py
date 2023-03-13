# String, Depth-First Search, Design, Trie
class WordDictionary:

    def __init__(self, is_end=False):
        self.links = {}
        self.is_end = is_end

    # Time complexity: O(M), where M is the key length.
    # At each step, we either examine or create a node in the trie.
    # That takes only M operations.

    # Space complexity: O(M).
    # In the worst-case newly inserted key doesn't share a prefix
    # with the keys already inserted in the trie.
    # We have to add M new nodes, which takes O(M) space.
    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.links:
                new_obj = WordDictionary()
                curr.links[w] = new_obj
                curr = curr.links[w]
            else:
                curr = curr.links[w]
        curr.is_end = True

    # Time complexity: O(M) for the "well-defined" words without dots,
    # where M is the key length.
    # and O(M⋅26^M) for the "undefined" words,
    # if we have a wildcard, '.',
    # we will have at most 26 keys, which leads to O(26^M),
    # as the branching factor is 26 and the depth is M, length of the word.
    # Now, the only other thing we have to consider is performing a substring activity on the word,
    # which is of length M. Thus time complexity is O(M⋅26^M) for the "undefined" words.

    # Space complexity: O(1) for the search of "well-defined" words without dots,
    # and up to O(M) for the "undefined" words, to keep the recursion stack.
    def search(self, word: str) -> bool:
        def dfs(word, node):
            for index, element in enumerate(word):
                if element == '.':
                    for key, value in node.links.items():
                        if dfs(word[index + 1:], value):
                            return True
                    return False
                else:
                    if element not in node.links:
                        return False
                    else:
                        node = node.links[element]
            return node.is_end

        return dfs(word, self)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


class AnotherSolutionWordDictionary:

    def __init__(self):
        self.links = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.links:
                curr.links[w] = AnotherSolutionWordDictionary()
            curr = curr.links[w]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return True if node.is_end else False
            if word[index] != '.' and word[index] not in node.links:
                return False
            if word[index] == '.':
                for key, value in node.links.items():
                    if dfs(value, index + 1):
                        return True
                return False
            else:
                return dfs(node.links[word[index]], index + 1)

        return dfs(self, 0)
