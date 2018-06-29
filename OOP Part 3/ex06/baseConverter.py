from stack import Stack


def baseConverter(decNum, base):
    s = Stack()
    decNum = int(decNum)
    base = int(base)
    if decNum < 0:
        print("Only positive decimal numbers allowed")
        return
    if (base <= 16) and (base >= 2):
        number = decNum
        while number > 0:
            remaindigit = (number % base) % 10
            number = number // base
            s.push(remaindigit)
    else:
        print("base should be from 2 to 16")
        return

    x = str(s) + " "
    x = x.replace(" ","")
    print(x)


if __name__ == "__main__":
    dNum = input("Enter the decimal number: ")
    bas = input("Enter the base: ")
    baseConverter(dNum, bas)
