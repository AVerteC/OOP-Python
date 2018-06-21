class SinglyList(object):
    def __init__(self):
        self.h = None

    def print_list(self,list_head):
            iterpos = iter(self)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)
            print(next(iterpos).content)




        # print(SinglyList.head)
        # print(SinglyList.__iter__(self))

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def head(self):
        return self.h

    @head.setter
    def head(self, val):
        self.h = val

    def isEmpty(self):
        return self.head == None

    def add_head(self, node):
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node