from singlylist_class import SinglyList
from node_class import Node


class LinkBuilder():
    def __init__(self):
        print("creating head of list")
        sl = SinglyList()

        for x in range(0, 10):
            print("creating node " + str(x))
            sl.add_head(Node(x))
            print(sl.head)
            print(sl)

