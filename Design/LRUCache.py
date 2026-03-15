class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.hmap = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self,node: Node):
        end = self.tail.prev
        end.next = node
        node.prev = end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def put(self,key:int, val:int):
        if key in self.hmap:
            oldNode = self.hmap[key]
            self.remove(oldNode)
        newNode = Node(key,val)
        self.add(newNode)
        self.hmap[key] = newNode

        if len(self.hmap) > self.cap:
            firstNode = self.head.next
            self.remove(firstNode)

    def get(self,key:int):
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        self.remove(node)
        self.add(node)
        return node.val



