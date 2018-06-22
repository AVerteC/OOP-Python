from node_class import Node
class SinglyList(object):
    def __init__(self):
        self.h = None

    def print_list(self, list_head):
        while list_head is not None:
            print(list_head.content)
            list_head = list_head.next

    def add_tail(self, list_head, val):
        endNode = Node(val)
        if list_head is None:
            list_head = endNode
            return
        lastNode = list_head
        while(lastNode.next):
            lastNode = lastNode.next
        lastNode.next = endNode

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def head(self):
        return self.h

    @head.setter
    def head(self, val):
        self.h = val

    def isEmpty(self):
        return self.head == None

    def add_head(self, node):
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node