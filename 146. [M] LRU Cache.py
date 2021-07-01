# https://leetcode.com/problems/lru-cache/

# Design a data structure that follows the constraints
# of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with
# positive size capacity.

# int get(int key) Return the value of the key if the key
# exists, otherwise return -1.

# void put(int key, int value) Update the value of the key
# if the key exists. Otherwise, add the key-value pair to
# the cache. If the number of keys exceeds the capacity
# from this operation, evict the least recently used key.

# The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self, key, val, pre=None, nex=None):
        self.key, self.val = key, val
        self.pre, self.nex = pre, nex


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.used = 0
        self.key_node = dict()
        self.head = Node(key=0, val=0)  # dummy node
        self.tail = Node(key=0, val=0)  # dummy node
        self.connect_nodes(self.head, self.tail)

    def get(self, key: int) -> int:
        if key in self.key_node:
            self.mark(self.key_node[key])
            return self.key_node[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            self.key_node[key].val = value
            self.mark(self.key_node[key])
            return
        elif self.used == self.cap:
            self.remove_one()

        # add the node
        new_node = Node(key=key, val=value, pre=self.head, nex=self.head.nex)
        self.key_node[key] = new_node
        self.connect_nodes(new_node, self.head.nex)
        self.connect_nodes(self.head, new_node)
        self.used += 1

    def mark(self, node: Node):
        pre, nex = node.pre, node.nex
        self.connect_nodes(pre, nex)
        self.connect_nodes(node, self.head.nex)
        self.connect_nodes(self.head, node)

    def remove_one(self):
        node = self.tail.pre
        assert(node != self.head)
        del self.key_node[node.key]
        self.used -= 1
        self.connect_nodes(node.pre, node.nex)

    @staticmethod
    def connect_nodes(a, b):
        a.nex, b.pre = b, a

    def iterate(self):
        ptr = self.head
        print('---------sdf----------')
        while ptr is not None:
            print(ptr.key, ptr.val)
            ptr = ptr.nex

if __name__ == '__main__':
    lru = LRUCache(capacity=2)
    print(lru.put(1,1))
    print(lru.put(2,2))
    print(lru.get(1))
    print(lru.put(3,3))
    print(lru.get(2))
