from singlylist_class import SinglyList
from node_class import Node

if __name__ == "__main__":

    print("creating head of list")
    sl = SinglyList()

    for x in range(0, 10):
        print("creating node " + str(x))
        sl.add_head(Node(x))


    sl.print_list(sl.head)