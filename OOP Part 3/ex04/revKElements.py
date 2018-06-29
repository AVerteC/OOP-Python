from stack import Stack
from queue import Queue


def revKElements(input_string, k):
    k = int(k)
    Listqu = Queue()
    Kst = Stack()
    Fst = Stack()
    input_string = input_string.replace(","," ")
    input_string = input_string.split(" ")

    if k > len(input_string):
        print("You cannot reverse more items than are in the input.")
        return

    for x in range(0, len(input_string)):
        Listqu.enqueue(input_string[x])

    for x in range(0, k):
        Kst.push(input_string[x])

    remainqueue = []

    for x in range(0, k):
        Listqu.dequeue()

    final = str(Kst) + str(Listqu)
    final = final.replace(" ",",")

    print(final[0:len(final)-1])


if __name__ == "__main__":
    instring = input("Enter the list of numbers: ")
    knum = input("Enter k: ")
    revKElements(instring, knum)
