from queue import Queue

if __name__ == "__main__":

    q = Queue()
    for x in range(4):
        print("adding queue item: " + str(x))
        # enqueue test
        q.enqueue(x)

    # size test
    print("size: " + str(q._size))

    # emptiness test
    print("empty? " + str(q.isEmpty))
    print(str(q))
    # print("front " + str(q.front))
    # print(q.front.next)
    # print("back " + str(q.back))
    # dqueue test
    # q.dequeue()
    # print(str(q))
