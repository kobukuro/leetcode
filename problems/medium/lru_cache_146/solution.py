# Tags: Hash Table, Linked List, Design, Doubly-Linked List
# reference: https://youtu.be/7ABFKPK2hD4


class Node:
    """Doubly linked list node for LRU Cache."""

    def __init__(
            self,
            key: int = 0,
            val: int = 0,
            prev: 'None | Node' = None,
            next: 'None | Node' = None,
    ):
        """
        Initialize a Node.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation.

    Uses a hash map for O(1) lookups and a doubly linked list
    to maintain access order. Most recently used items are near
    the right end, least recently used items are near the left end.

    Time complexity: O(1) for both get and put operations.
    Space complexity: O(capacity) for the hash map and doubly linked list.
    """

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        """
        Remove a node from the doubly linked list.

        Args:
            node: The node to remove.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        prev = node.prev
        nxt = node.next
        node.prev = None
        node.next = None
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node) -> None:
        """
        Insert a node right before the right sentinel (most recently used position).

        Args:
            node: The node to insert.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev

    def get(self, key: int) -> int:
        """
        Get the value associated with the key.

        Moves the accessed node to the most recently used position.

        Args:
            key: The key to look up.

        Returns:
            The value if key exists, otherwise -1.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair.

        If the key exists, update the value and move to most recently used.
        If the key doesn't exist, create a new node and insert it.
        If capacity is exceeded, evict the least recently used item.

        Args:
            key: The key to insert or update.
            value: The value to associate with the key.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(self.cache[key])
        if len(self.cache) > self.size:
            lru_key = self.left.next.key
            self.remove(self.left.next)
            del self.cache[lru_key]
