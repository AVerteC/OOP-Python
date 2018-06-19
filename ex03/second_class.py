from first_class import FirstClass


class SecondClass(FirstClass):
    def __init__(self, name):
        super().say_hello(name)