class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  
        self.capacity = capacity
        self.size = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.moveFront(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveFront(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.addToFront(new_node)
            self.size+=1

            if self.size > self.capacity:
                lru = self.tail.prev
                self.removeNode(lru)
                del self.cache[lru.key]
                self.size-=1

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToFront(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def moveFront(self, node):
        self.removeNode(node)
        self.addToFront(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)