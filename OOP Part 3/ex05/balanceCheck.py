#AVerteC
def check_parentheses(s):
    # total parentheses value
    mtotal = 0
    for c in s:
        if c == "(":
            mtotal += 1
        if c == ")":
            mtotal -= 1

    # block failure state of )(
        if mtotal < 0:
            return False
    # pass
    if mtotal == 0:
        return True
    # fail
    else:
        return False


def check_squarebracket(s):
    # total parentheses value
    mtotal = 0
    for c in s:
        if c == "[":
            mtotal += 1
        if c == "]":
            mtotal -= 1

    # block failure state of )(
        if mtotal < 0:
            return False
    # pass
    if mtotal == 0:
        return True
    # fail
    else:
        return False


def check_curlybracket(s):
    # total parentheses value
    mtotal = 0
    for c in s:
        if c == "{":
            mtotal += 1
        if c == "}":
            mtotal -= 1

    # block failure state of )(
        if mtotal < 0:
            return False
    # pass
    if mtotal == 0:
        return True
    # fail
    else:
        return False


def main():
    instr = input("Enter the sequence: ")
    if len(instr) == 0:
        print("True")
        return True
    if not("(" or ")") or not("[" or "]") or not("{" or "}"):
        print("True")
        return True

    x = check_curlybracket(instr)
    y = check_parentheses(instr)
    z = check_squarebracket(instr)
    if x == y == z:
        print("True")
        return True
    print("False")
    return False


main()
