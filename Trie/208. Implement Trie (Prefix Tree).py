# Hash Table, String, Design, Trie
class Trie:

    def __init__(self, is_end=False):
        self.links = {}
        self.is_end = is_end

    # Time complexity : O(m), where m is the key length.
    # In each iteration of the algorithm,
    # we either examine or create a node in the trie till we reach the end of the key.
    # This takes only m operations.

    # Space complexity : O(m).
    # In the worst case newly inserted key doesn't share
    # a prefix with the the keys already inserted in the trie.
    # We have to add m new nodes, which takes us O(m) space.
    def insert(self, word: str) -> None:
        curr_node = self
        for w in word:
            if w not in curr_node.links:
                new_obj = Trie()
                curr_node.links[w] = new_obj
                curr_node = new_obj
            else:
                curr_node = curr_node.links[w]
        curr_node.is_end = True

    # Time complexity : O(m)
    # In each step of the algorithm we search for the next key character.
    # In the worst case the algorithm performs m operations.

    # Space complexity : O(1)
    def search(self, word: str) -> bool:
        curr_node = self
        for w in word:
            if w not in curr_node.links:
                return False
            else:
                curr_node = curr_node.links[w]
        return curr_node.is_end

    # Time complexity : O(m)
    # Space complexity : O(1)
    def startsWith(self, prefix: str) -> bool:
        curr_node = self
        for w in prefix:
            if w not in curr_node.links:
                return False
            else:
                curr_node = curr_node.links[w]
        return True
