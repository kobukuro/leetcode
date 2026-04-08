# Tags: Hash Table, String, Design, Trie


class Trie:

    def __init__(self):
        self.links: dict[str, Trie] = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        """
        Time complexity : O(m), where m is the key(word) length.
        In each iteration of the algorithm,
        we either examine or create a node in the trie till we reach the end of the key.
        This takes only m operations.

        Space complexity : O(m).
        In the worst case newly inserted key doesn't share
        a prefix with the keys already inserted in the trie.
        We have to add m new nodes, which takes us O(m) space.
        """
        curr = self
        for c in word:
            if c not in curr.links:
                curr.links[c] = Trie()
            curr = curr.links[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        """
        Time complexity : O(m)
        In each step of the algorithm we search for the next key character.
        In the worst case the algorithm performs m operations.

        Space complexity : O(1)
        """
        curr = self
        for c in word:
            if c not in curr.links:
                return False
            curr = curr.links[c]
        return curr.is_end

    def starts_with(self, prefix: str) -> bool:
        """
        Time complexity : O(m)

        Space complexity : O(1)
        """
        curr = self
        for c in prefix:
            if c not in curr.links:
                return False
            curr = curr.links[c]
        return True
