from node_nerf import Node

class Queue:
    def __init__(self, front=None ):
        self.front = front
        self.back = None
        self._size = 0

    @property
    def isEmpty(self):
        if self.front is None:
            return True
        return False

    # add item
    def enqueue(self, data):
        if self.front is None:
            fNode = Node(data)
            self.front = fNode
            self.back = fNode
            self._size += 1
        else:
            cNode = Node(data)
            cNode.next = self.front
            self.back = cNode
            self._size += 1

    # remove item

    def dequeue(self):
        self.back = self.front.next
        self._size -= 1

    def front(self):
        return self.front

    @property
    def size(self):
        return self._size

    @property
    def __str__(self):
        fullstr = ""
        while self.front is not None:
            fullstr += str(self.front.data) + " "
            self.front = self.front.next
        return fullstr
