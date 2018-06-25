from stack import Stack
from node_nerf import Node

if __name__ == "__main__":

    #print("creating head of list")
    sl = Stack(10)

    for x in range(4):
        sl.push(x)
    print(sl)
    print(" ")
    sl.push(20)
    print(" ")
    print(sl)
    print(" ")
    sl.pop(20)
    print(sl)
