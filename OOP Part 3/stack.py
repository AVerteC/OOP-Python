from node_nerf import Node
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    @property
    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):
        # brand new top's next is the current top
        if self.size is None:
            tNode = Node(data)
            self.top = tNode
            self._size += 1
        cNode = Node(data)
        cNode.next = self.top
        self.top = cNode
        self._size += 1

    @property
    def pop(self):
        if self.top is None:
            return None
        self.top = self.top.next
        self._size -= 1

    @property
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    @property
    def size(self):
        return self._size

    def __str__(self):
        fullstr = ""
        while self.top is not None:
            fullstr += str(self.top.data) + " "
            self.top = self.top.next
        return fullstr
