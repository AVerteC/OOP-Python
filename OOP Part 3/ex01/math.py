from stack import Stack


if __name__ == "__main__":
    mst = Stack()
    x = input("Enter the numbers: ")

    # separate numbers
    data = x.split(",")
    sum = 0
    # add numbers to stack and remove whitespace
    for x in range(0, len(data)):
        data[x] = str(data[x]).replace(" ", "")
        mst.push(int(data[x]))
    product = mst.peek
    min = 9999
    max = -9999
    maxsize = mst.size
    for x in range(0, mst.size):
        sum += mst.peek
        if mst.peek < min:
            min = mst.peek
        if mst.peek > max:
            max = mst.peek
        # print("current:"+str(mst.peek))
        mst.pop
        if mst.peek is not None:
            product *= mst.peek
        """
        print("sum:"+str(sum))
        print("product:"+str(product))
        print("min:"+str(min))
        print("max:"+str(max))
        """
    mean = sum/maxsize
    print("Total count = " + str(maxsize))
    print("Sum = " + str(sum))
    print("Product = " + str(product))
    print("Mean = " + str(mean))
    print("Min = " + str(min))
    print("Max = "+ str(max))



