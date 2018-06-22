from singlylist_class import SinglyList
from node_class import Node

if __name__ == "__main__":

    print("creating head of list")
    sl = SinglyList()

    for x in range(4):
        sl.add_head(Node(x))
    sl.print_list(sl.head)
    sl.add_tail(sl.head, 20)
    sl.print_list(sl.head)
