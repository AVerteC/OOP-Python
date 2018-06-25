class Stack:
    def __init__(self, top):
        self.top = top
        self.size = 0
        self.next = None

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):
        self.next = self.top
        self.top = data
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        self.top = self.next
        self.size -= 1

    def peek(self):
        if self.top is None:
            return None
        return self.top

    def size(self):
        return self.size

    def __str__(self):
        output = ""
        while self.top is not None:
            output += str(self.top.peek) + ", "
            self.top = self.top.next
        print(output)
