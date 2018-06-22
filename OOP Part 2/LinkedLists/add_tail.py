from node_class import Node
def add_tail(self, list_head, val):
    endNode = Node(val)
    if list_head is None:
        list_head = endNode
        return
    lastNode = list_head
    while (lastNode.next):
        lastNode = lastNode.next
    lastNode.next = endNode