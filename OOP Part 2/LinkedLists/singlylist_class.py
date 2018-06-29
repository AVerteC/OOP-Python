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
        LastNode = list_head
        while LastNode.next:
            LastNode = LastNode.next
        LastNode.next = endNode

    def remove(self, list_head, val):
        if list_head is not None:
            if list_head == val:
                list_head = list_head.next
                list_head = None
                return
        while list_head is not None:
            if list_head.content == val:
                break
            back = list_head
            list_head = list_head.next

        if list_head is None:
            return
        back.next = list_head.next

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

    def has_cycle(self, list_head):
        if list_head is None:
            return True
        if list_head.next is not None:
            return True




