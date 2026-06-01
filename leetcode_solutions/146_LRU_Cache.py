# Node and LRUCache implementation with per-line comments explaining each statement

class Node:  # Define a doubly linked list node type used by the LRU cache
    # Docstring describing Node usage
    """
    Doubly linked list node.
    __slots__ saves ~40% memory vs default __dict__.
    In a cache holding millions of entries this matters.
    """
    __slots__ = ("key", "val", "prev", "next")  # Limit instance attributes to these four names

    def __init__(self, key: int = 0, val: int = 0) -> None:  # Constructor with default key/val
        self.key  = key  # Store the node's key for hashmap deletion on eviction
        self.val  = val  # Store the node's value returned by get()
        self.prev: "Node | None" = None  # Pointer to previous node in the list
        self.next: "Node | None" = None  # Pointer to next node in the list


class LRUCache:  # LRU cache class using hashmap + doubly linked list
    """
    O(1) get and put using HashMap + Doubly Linked List.

    Structure:
        HEAD <-> [MRU] <-> ... <-> [LRU] <-> TAIL
        HashMap: key -> Node

    HEAD and TAIL are sentinel nodes — never evicted,
    eliminate edge case checks in every operation.
    """

    def __init__(self, capacity: int) -> None:  # Initialize cache with fixed capacity
        if capacity <= 0:  # Validate capacity is positive
            raise ValueError(f"Capacity must be positive, got {capacity}")  # Raise on invalid capacity
        self.capacity = capacity  # Store maximum number of items allowed in cache
        self.cache: dict[int, Node] = {}  # HashMap from key to Node for O(1) access

        # Sentinel nodes
        self.head = Node()   # dummy head — MRU side (most recently used side)
        self.tail = Node()   # dummy tail — LRU side (least recently used side)
        self.head.next = self.tail  # Initially, head points to tail directly
        self.tail.prev = self.head  # Tail points back to head directly

    # ── Private helpers ───────────────────────────────────────────────────────

    def _remove(self, node: Node) -> None:  # Remove a node from its position in the list
        """
        Unlink node from its current position in the list.
        Connects node's neighbours directly to each other.

        Before: ... <-> A <-> node <-> B <-> ...
        After:  ... <-> A <-> B <-> ...
        """
        node.prev.next = node.next  # Bypass node by making previous node point to node.next
        node.next.prev = node.prev  # Bypass node by making next node point back to node.prev

    def _insert_front(self, node: Node) -> None:  # Insert node right after head to mark MRU
        """
        Insert node immediately after HEAD (mark as most recently used).

        Before: HEAD <-> first <-> ...
        After:  HEAD <-> node <-> first <-> ...
        """
        node.next          = self.head.next  # New node's next becomes the current first real node
        node.prev          = self.head  # New node's prev points to head sentinel
        self.head.next.prev = node  # Current first node's prev updated to the new node
        self.head.next     = node  # Head's next updated to new node, completing insertion

    # ── Public API ────────────────────────────────────────────────────────────

    def get(self, key: int) -> int:  # Retrieve value for key and mark as MRU
        """
        Return value for key, or -1 if not found.
        Marks the key as most recently used.
        
        Time: O(1)
        """
        if key not in self.cache:  # If key absent in hashmap
            return -1  # Indicate missing entry per problem spec

        node = self.cache[key]  # Retrieve the node from hashmap in O(1)
        # Move to front — this is the "recently used" part
        self._remove(node)  # Unlink node from its current position
        self._insert_front(node)  # Insert node immediately after head as MRU
        return node.val  # Return the stored value

    def put(self, key: int, val: int) -> None:  # Insert or update key with value
        """
        Insert or update key. Evicts LRU item if over capacity.
        
        Time: O(1)
        """
        if key in self.cache:  # If key already exists in cache
            # Update existing — remove from current position
            self._remove(self.cache[key])  # Remove the old node from the list

        # Create new node and insert at front
        node = Node(key, val)  # Make a fresh node storing key and value
        self._insert_front(node)  # Place it at MRU position right after head
        self.cache[key] = node  # Update hashmap to point to the new node

        if len(self.cache) > self.capacity:  # If we exceeded capacity after insertion
            # Evict LRU — the node just before TAIL
            lru = self.tail.prev  # The LRU item is the node before the tail sentinel
            self._remove(lru)  # Unlink the LRU node from the list
            del self.cache[lru.key]  # Remove corresponding entry from hashmap
            # Note: we store key in Node so we can delete from hashmap here


    # ── Debug helper ─────────────────────────────────────────────────────────

    def __repr__(self) -> str:  # String representation showing MRU -> LRU order
        """Show cache state MRU → LRU for debugging."""
        items = []  # Collect key:value pairs for display
        curr = self.head.next  # Start traversal from the node after head (MRU)
        while curr != self.tail:  # Traverse until hitting tail sentinel
            items.append(f"{curr.key}:{curr.val}")  # Append textual representation
            curr = curr.next  # Move to the next node in order
        return f"LRUCache([{ ' -> '.join(items) }], cap={self.capacity})"  # Return formatted string


# Explanatory comments and usage examples
# The Node class represents a node in a doubly linked list. It stores a key and
# value and pointers to the previous and next nodes. Using __slots__ avoids a
# per-instance __dict__, reducing memory overhead for large caches.
#
# The LRUCache uses a hashmap (self.cache) for O(1) access from a key to its
# corresponding Node, and a doubly linked list to track usage order from most
# recently used (MRU, next to head) to least recently used (LRU, next to tail).
# Two sentinel nodes (head and tail) simplify insertions/removals by avoiding
# checks for None at the ends.
#
# Key operations:
# - _remove(node): unlink a node from its current position by reconnecting its
#   neighbours. This is O(1) because we have direct pointers to prev/next.
# - _insert_front(node): insert a node immediately after the head sentinel,
#   marking it as the most recently used. Also O(1).
# - get(key): if present, move the node to the front (MRU) and return its value;
#   otherwise return -1.
# - put(key, val): if key exists, remove the old node; create a new node and
#   insert it at the front. If adding causes capacity to be exceeded, evict the
#   LRU node (the one just before the tail) and remove its key from the hashmap.
#
# Correctness notes:
# - Storing the key in the node lets us efficiently remove the key from the
#   hashmap when evicting the LRU node.
# - Sentinel head and tail nodes ensure that _remove and _insert_front never
#   have to handle None pointers for neighbours.
# - All public operations are O(1) time.
#
# Example usage:
# from pathlib import Path
# # import by file path if module name is not a valid identifier
# import importlib.util
# p = Path(__file__).resolve()
# spec = importlib.util.spec_from_file_location("lru_module", str(p))
# mod = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(mod)
# c = mod.LRUCache(2)
# c.put(1, 1)
# c.put(2, 2)
# assert c.get(1) == 1  # 1 becomes MRU
# c.put(3, 3)           # evicts key 2 (LRU)
# assert c.get(2) == -1
#
# End of explanatory comments