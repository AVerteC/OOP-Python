from stack import Stack
from node_nerf import Node


def strrev():
    s = Stack()
    x = input("Enter the string to be reversed: ")
    for z in range(0, len(x)):
        print(x[z])
        s.push(x[z])
    print("Reversed String: ", end="")
    for z in range(0, len(x)):
        print(s.peek, end="")
        s.pop

if __name__ == "__main__":
    strrev()


