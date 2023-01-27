# Hash Table, String, Design, Trie
class Trie:

    def __init__(self, is_end=False):
        self.links = {}
        for i in range(97, 123):
            self.links[chr(i)] = None
        self.is_end = is_end

    def insert(self, word: str) -> None:
        curr_node = self
        for w in word:
            if curr_node.links[w] is None:
                new_obj = Trie()
                curr_node.links[w] = new_obj
                curr_node = new_obj
            else:
                curr_node = curr_node.links[w]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self
        for w in word:
            if curr_node.links[w] is None:
                return False
            else:
                curr_node = curr_node.links[w]
        return curr_node.is_end

    def startsWith(self, prefix: str) -> bool:
        curr_node = self
        for w in prefix:
            if curr_node.links[w] is None:
                return False
            else:
                curr_node = curr_node.links[w]
        return True
