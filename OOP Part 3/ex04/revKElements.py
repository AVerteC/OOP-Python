from stack import Stack
from queue import Queue


def revKElements(input_string, k):
    k = int(k)
    Listqu = Queue()
    Kst = Stack()
    input_string = input_string.replace(","," ")
    input_string = input_string.split(" ")

    for x in range(0, len(input_string)):
        Listqu.enqueue(input_string[x])

    for x in range(0, k):
        Kst.push(input_string[x])

    print(Kst)
    print(Listqu)


if __name__ == "__main__":
    instring = input("Enter the list of numbers: ")
    knum = input("Enter k: ")
    revKElements(instring, knum)
