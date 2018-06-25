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
        mst.push(float(data[x]))
    for x in range(0, mst.size):
        
        product *= data[x]
    print(data)
    print("Total count = " + str(mst.size))
    print("Sum = " + str(sum))
    print("Product = " + str(product))


